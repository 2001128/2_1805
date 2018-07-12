class Animal():
        
    def wark(self):
        print("叫")


class Dog(Animal):
   
    def wark(self):#重写
        print("汪汪叫")



class xiaotianquan(Dog):
    
    def wark(self):#重写
        print("狂叫")
        #Dog.wark(self)#调用父类方法
        super().wark()
d = Dog()
d.wark()

xtq = xiaotianquan()
xtq.wark()

