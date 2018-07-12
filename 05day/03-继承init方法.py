class Animal(object):

    def __init__(self,name,color = "白色"):
        self.name = name
        self.color = color
    def eat(self):
        print("吃东西")

    def setColor(self,color):
        self.color = color

    def __str__(self):
        msg = "颜色是%s"%self.color
        return msg
'''
子类没有init方法 但是父类有，当实例化对象的时候
默认执行init
'''
'''
私有属性和私有方法到底能不能被继承
不能继承的话 子类怎么间接获取私有属性和私有方法
'''
class Cat(Animal):

    def uptree(self):
        print("上树")


bosi = Cat("波斯猫","黑色")
bosi.uptree()
bosi.eat()

bosi.setColor("绿色")

print(bosi)
