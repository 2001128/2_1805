def w1(id):
    def w2(fun):
        def w3(*args,**kwargs):
            if id == 1:
                print ("验证成功")
                ret = fun(*args,**kwargs)
                return ret 
            else:
                print("验证失败")
                return 0
        return w3
    return w2


@w1(id = 1)
def getMoney():
    return 500000

@w1(id = 1)
def setMoney(money):
    print("要存%f"%money) 

@w1(id = 2)   
def otherGetMoney():
    return 500000
ret = getMoney()
print("本人要取%f"%ret)  

setMoney(100)

ret1 = otherGetMoney()
print("其他人要取钱%f"%ret1)             
