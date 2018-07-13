class Dog():
    __instance = None
    def __new__(cls,*args,**kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
    def __init__(self,name):
        self.name = name
dog1 = Dog("laowang")
dog2 = Dog("laosong")
dog3 = Dog("laozhao")
print(id(dog1))
print(id(dog2))
print(id(dog3))

