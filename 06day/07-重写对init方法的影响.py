class Dog():
    __instance = None#类属性
    __flag = False#类属性
    def __init__(self,name):
        print("init")
        if Dog.__flag == False:
            self.name = name
            Dog.__flag = True

    def __str__(self):
        print("str")
        return "哈哈"

    def __del__(self):
        print("del")
    
    def __new__(cls,*args,**kwargs):#创建对象的方法
       print("new")
       if cls.__instance != None:
           return cls.__instance
       else:
            cls.__instance = object.__new__(cls)
       return cls.__instance
    

dog = Dog("1")
print(dog)
print(id(dog))

dog1 = Dog("2")
print(dog1)
print(id(dog1))

dog2 = Dog("3")
print(dog2)
print(id(dog2))

print(dog.name)
