class Cat():
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
   # def introduce(self):
    #    print("我的名字是%s 年龄是%d"%(self.name,self.age))

    def __str__(self):#一定要返回值
        return "我的名字是%s 年龄%d"%(self.name,self.age)
tom = Cat("tom",12)#创建实例对象
#tom.introduce()
#print(id(tom))    
print(tom)    
