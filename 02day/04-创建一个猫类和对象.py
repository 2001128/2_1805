class Cat:

    def eat(self,food):
        print("%s吃%s"%(self.name,food))

    def miaomiao(self):
        print("喵喵")

    def introduce(self):
        print("我的名字是%s 我的颜色%s"%(self.name,self.color))


bosimao = Cat()
bosimao.color = "绿色"
bosimao.name = "波斯猫"
bosimao.eat("鲨鱼")
bosimao.miaomiao()
bosimao.introduce()

tom = Cat()
tom.color = "蓝色"
tom.name = "汤姆"
tom.eat("金鱼")
tom.miaomiao()
tom.introduce()

