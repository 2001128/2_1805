from multiprocessing import Manager,Pool
import time
i = 0
def banzhuan(q):
    for i in range(5):
        time .sleep(1)
        q.put("第%d块砖"%i)
        print("放了%d块砖"%i)

def qiqiang(q):
    while True:
        if q.empty() == False:
            for i in range(q.qsize()):
                time.sleep(1)
                print(q.get())
        
p = Pool()
q = Manager().Queue()

p.apply_async(banzhuan,(q,))
p.apply_async(qiqiang,(q,))
p.close()
p.join()
