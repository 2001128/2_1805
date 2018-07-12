class Person(object):

    def __init__(self,name):
        self.name = name
        self.__money = 1000
        

    def getMoney(self):
        return self.__money

    def setMoney(self):
        self.__money = 1000000
   
    def __play(self):
        print("玩")

    def play(self):
        self.__play()

    def sleep(self):
        print("睡觉")

    def speak(self):
        print("说话")



class Man(Person):

    def inMoney(self):
        print("赚钱")


class Woman(Person):

    def outMoney(self):
        print("花钱")


caizijian = Man("柴子健")
print(caizijian.getMoney())
caizijian.play()
caizijian.speak()
caizijian.sleep()
caizijian.inMoney()


xiaonannan = Woman("小楠楠")
xiaonannan.speak()
xiaonannan.sleep()
xiaonannan.outMoney()

