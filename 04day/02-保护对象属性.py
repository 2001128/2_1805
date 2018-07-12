class Dog():
    def __init__(self):
        self.age = 1

    def wark(self):
        print("汪汪")

    def setage(self,age):#设置属性
        if age <= 0:
            print("不合法")
        else:
            self.age = age
    def getage(self):#获取属性
        return self.age

jinmao = Dog()
#jinmao.age =  -10
jinmao.setage(10)
#print(jinmao.age)
print(jinmao.getage())
