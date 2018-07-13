class Cat(object):
    __instance = None
    __flag = False
    def __new__(cls):#创建对象的方法
           print("new")
           if cls.__instance != None:
               return cls.__instance
           else:
                cls.__instance = object.__new__(cls)
           return cls.__instance
    def __init__(self):
                
c = Cat()
