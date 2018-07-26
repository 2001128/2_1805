from multiprocessing import Pool
import time 

def work(msg):
    for i in range(10):
        time.sleep(1)
        print("嘿嘿嘿%s"%msg)

p = Pool(3)#最大装3个进程

for i in range(6):
    p.apply_async(work,(i,))#非阻塞
    #p.apply(work,(i,))#阻塞
    print("添加一个")

p.close()
p.join()
