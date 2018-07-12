'''
房子类
家具类
'''

list = []

class Home():
    

   def __init__(self,address,area):

       self.address = address
       self.area = area
       self.list =  []

   def __str__(self):#打印实例对象
      msg = "我的家在%s 面积是%d"%(self.address,self.area)
      return msg

   def zhuangjiaju(self,jiaju):
        if self.area < jiaju.area:
            print("不能再装了")
        else:
            self.list.append(jiaju) 
            self.area = self.area - jiaju.area
   
    def tellArae(self):
        return 剩余的面积

class Bed():

    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        msg = "牌子是%s 大小是%d"%(self.name,self.area)
        return msg

laowang = Home("北京市长安大街666号",1000)
print(laowang)

ximengsi = Bed("席梦思",5)

for i  in range(300):
    #获取房子的剩余面积 如果小于你要装家具的面积 就直接break
    laowang.zhuangjiaju(ximengsi)

