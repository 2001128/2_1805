class Person():
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def  introduce(self):
          print("我叫%s 我的年龄是%d"%(self.name,self.age))



name = input("请输入名字")
age = int(input("请输入年龄"))
laowang = Person(name,age)
laowang.introduce()

