from multiprocessing import Process
import time

class MyProcess(Process):

    def __init__(self,name):
        super().__init__()
        self.name = name
        
    def run (self):
        for i in range(10):
            time.sleep(1)
            print("我重写了run方法%s"%self.name)


p = MyProcess("老王")
p1 = MyProcess("老宋")
p.start()
p1.start()
p.join()
p1.join()
print("我是主进程")
