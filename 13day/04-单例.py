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

dog1 = Dog("老王")
dog2 = Dog("老宋")

print(id(dog1))
print(id(dog2))
