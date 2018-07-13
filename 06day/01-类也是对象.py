
#list = []

class Dog():
    count = 0#类属性
    def __init__(self):#魔法方法
        Dog.count+=1#修改类属性
        self.name = "laowang"#实例化对象属性


    def wark(self):#实例化方法
        print("汪汪叫")

    @classmethod
    def getCount(cls):
        return cls.count



dog = Dog()#初始化实例对象
dog.wark()
#list.append(dog)
#count+=1

dog1 = Dog()
dog1.wark()
#list.append(dog1)
#count+1

#print(Dog.count)
#print(len(list))
print(Dog.getCount())#通过类调用类方法
print(dog1.getCount())#通过对象调用类方法


'''
创建一个Tool类
统计创建工具类对象个数
并通过类方法获取个数
'''
