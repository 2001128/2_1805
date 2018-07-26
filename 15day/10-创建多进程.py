import os

p = os.fork()
if p == 0:
    print("子进程%d 父进程%d"%(os.getpid(),os.getppid()))
    print("子进程")
else:
    print("父进程")
