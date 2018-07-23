def w(type):
    def w1(fun):
        def inner():
            if type == 1:
                print("验证cf账号")
            elif type == 2:
                 print("验证王者账号")
            fun()
        return inner
    return w1
'''
    def w2(fun):
        def inner():
            print("验证王者账号")
            fun()
        return inner
'''
@w(1)
def play1():
    print("我要玩cf")

@w(2)
def play2():
    print("我要打王者")

play1()
play2()
