class Dog():
    
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "我的名字是%s"%self.name

    def __del__(self):
        print("我要死了")

    def wark(self):
        print("汪汪叫")

