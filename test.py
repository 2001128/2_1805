def fib(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
        temp = yield b
        print(temp)
#f = fib(5)
#for i in f:
    #print(i)
