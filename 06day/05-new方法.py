class Dog():
    i = 0
    j = None
    def __init__(self):
        print("init")
        self.name = "tom"
    
    def __str__(self):
        print("str")
        return "哈哈"

    def __del__(self):
        print("del")
    
    def __new__(cls):#创建对象的方法
       print("new")
       if cls.i == 1:
           return cls.j  
       else:
            cls.i = 1
            cls.j = object.__new__(cls)
       return cls.j
    

dog = Dog()
print(dog)
print(id(dog))

dog1 = Dog()
print(dog1)
print(id(dog1))

dog2 = Dog()
print(dog2)
print(id(dog2))



