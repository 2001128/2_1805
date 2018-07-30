from threading import Thread

import time
num = 0

def work1():
    time.sleep(1)
    print("线程一%d"%num)

def work2():
    global num
    num+=1
    print("线程二%d"%num)

t = Thread(target=work1)
t1 = Thread(target=work2)
t.start()
t1.start()
