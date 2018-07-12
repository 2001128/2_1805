class Car():
    
    def __init__(self,color,size):#系统方法---初始化方法
        self.color = color
        self.name = "宝马"
        self.size = size
 
    def introduce(self):#自己定义的方法
        print("我的颜色是%s 我的大小是%d"%(self.color,self.size))

'''
self == bmw
bmw.color = "绿色" 相等于  self.color = "绿是"
'''
bmw = Car("绿色",12)#创建一个实例对象 初始化一个实例对象
#bmw.color = "绿色"
#bmw.size = 12
bmw.introduce()

bmx7 = Car("蓝色",13)
bmx7.introduce()
