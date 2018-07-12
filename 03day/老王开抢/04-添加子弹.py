class Person():#人类
	def __init__(self,name):
		self.name = name
		

	def zhuangzidan(self,danjia,zidan):
		danjia.list.append(zidan)#装子弹

	
	def zhuangdanjia(self,gun,danjia):#装弹夹
		gun.danjia = danjia


class Gun():#枪类
	def __init__(self,name):
		self.name = name
		self.danjia = None#假设没有弹夹

class DanJia():#弹夹类
	def __init__(self,name,count):
		self.name = name
		self.count = count
		self.list = []#装子弹




class ZiDan():#子弹
	def __init__(self,name):
		self.name = name


laowang = Person("老王")#创建老王
ak47 = Gun("ak47")#创建枪
danjia = DanJia("快速扩容",40)#创建弹夹

for i in range(40):#创建一些子弹
	zidan = ZiDan()
	laowang.zhuangzidan(danjia,zidan)

laowang.zhuangdanjia(ak47,danjia)#装弹夹

