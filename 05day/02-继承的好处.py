class Animal():
    
    def eat(self):
        print("吃东西")
   

class Dog(Animal):
    
    def wark(self):
        print("汪汪叫")
    

class Cat(Animal):
    def miaomiao(self):
        print("喵喵叫")

'''
继承的好处实现代码复用
'''
shabigou = Dog()
shabigou.wark()
shabigou.eat()


jiafeimao = Cat()
jiafeimao.miaomiao()
jiafeimao.eat()
