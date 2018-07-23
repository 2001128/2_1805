def w1(fun):
    def inner(*args,**kwargs):
        print("验证登录")
        return fun(*args,**kwargs)
    return inner


@w1
def play(a,b):
    print("%s,%s"%(a,b))
    return "hehe"
ret = play("藏獒","狂犬")
print(ret)

@w1
def play1():
    print("哈哈哈")
play1()


@w1
def play2(a):
    print("呵呵呵%s"%a)
play2("666")


@w1
def play3():
    return "嘻嘻嘻" 
ret = play3()
print(ret)        
