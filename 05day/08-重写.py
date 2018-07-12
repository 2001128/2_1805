class Animal():
        
    def wark(self):
        print("叫")


class Dog(Animal):
   
    def wark(self):
        print("汪汪叫")



class xiaotianquan(Dog):
    
    def wark(self):
        print("狂叫")
d = Dog()
d.wark()

xtq = xiaotianquan()
xtq.wark()
