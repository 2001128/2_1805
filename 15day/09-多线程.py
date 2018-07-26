import time
from threading import Thread
def sing():
    time.sleep(2)
    print("不是很安排但是很安排 安排~")


for i in range(5):
    t = Thread(target = sing)
    t.start()
print("做你的眼睛")
