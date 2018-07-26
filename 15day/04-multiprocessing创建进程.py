from multiprocessing import Process
import time 
def work(arg):
    for i in range(10):
        time.sleep(1)
        print("哈哈哈",arg) 
p = Process(target=work,args=("呵呵呵",))
p1 = Process(target=work,args=("嘿嘿嘿",))

p.start()#开启子进程
p1.start()
p.join(5)#等待子进程执行完毕
print("我是主进程")



           
