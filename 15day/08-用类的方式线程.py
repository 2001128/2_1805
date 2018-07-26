from threading import Thread
import time
class MyThread(Thread):

    def run(self):
        for i in range(10):
            time.sleep(1)
            print("嘿嘿嘿",self.name)

for i in range(2):
    t = MyThread()
    t.start()
