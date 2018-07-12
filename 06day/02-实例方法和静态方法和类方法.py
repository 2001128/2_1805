class NanNan():
    
    sex = "男"#类属性

    def __init__(self,name):#魔法方法初始化方法
        self.name = name#实例属性


    def getName(self):#实例方法
        return self.name

    def setName(self,name):#实例方法
        self.name = name

    @classmethod    
    def getSex(cls):#类方法
        return cls.sex#调用类属性

    @classmethod
    def setSex(cls,sex):#类方法
        cls.sex = sex

    @staticmethod
    def print_menu():#静态方法
        print("菜单")
        print("1、约我")
        print("2、请我吃饭")
        print("3、别说话")

xiaonannan = NanNan("小楠楠")#通过对象调用实例方法
xiaonannan.setName("小娜娜")#通过对象调用实例方法
print(xiaonannan.getName()) 

NanNan.setSex("女")
print(NanNan.getSex())#通过类调用类方法
print(xiaonannan.getSex())#通过对象调用类方法


NanNan.print_menu()#通过类方法调用静态方法
#xiaonannan.print_menu()#通过对象调用静态方法    
