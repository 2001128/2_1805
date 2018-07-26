from threading import Thread 
import time 
num = 0
flag = 1
def work():
    global num
    global flag
    if flag == 1:
        for i in range(1000000):
            num+=1
        flag = 2
    print("线程一:%d"%num)


def work1():
    global num
    while True:
        if flag == 2:
            for i in range(1000000):
                num+=1
            break
    print("线程二:%d"%num)


t = Thread(target=work)
t1 = Thread(target=work1)
t.start()
t1.start()

