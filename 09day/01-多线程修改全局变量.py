from threading import Thread

import time

num = 0

def name1():
    time.sleep(1)
    print("线程一%d"%num)


def name2():
    global num
    num += 1
    print("线程二%d"%num)


t = Thread(target=name1)
t1 = Thread(target=name2)

t.start()
t1.start()
