from threading import Thread,Lock 
import time 
num = 0
def work():
    global num
#    mutex.acquire(True)
    for i in range(1000000):
        mutex.acquire(True)
        num += 1
        mutex.release()
    #mutex.release()
    print("线程一:%d"%num)


def work1():
    global num
    #mutex.acquire(True)
    for i in range(1000000):
        mutex.acquire(True)
        num +=1
        mutex.release()
    #mutex.release()
    print("线程二:%d"%num)
mutex = Lock()#创建一把锁

t = Thread(target=work)
t1 = Thread(target=work1)
t.start()
t1.start()

