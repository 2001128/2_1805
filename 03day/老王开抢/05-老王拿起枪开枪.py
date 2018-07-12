class Person():#人类
	def __init__(self,name):
		self.name = name
		

	def naqiang(self,gun):
		self.gun = gun


	def zhuangzidan(self,danjia,zidan):
		danjia.list.append(zidan)#装子弹

	
	def zhuangdanjia(self,gun,danjia):#装弹夹
		gun.danjia = danjia

	def openGun(self,diren):#开枪
		zidan = self.gun.danjia.tanzidan()	
		zidan.kill(diren)

class Gun():#枪类
	def __init__(self,name):
		self.name = name
		self.danjia = None#假设没有弹夹

class DanJia():#弹夹类
	def __init__(self,name,count):
		self.name = name
		self.count = count
		self.list = []#装子弹

	def tanzidan(self):
		return zidan = self.list.pop()


class ZiDan():#子弹
	def __init__(self,name):
		self.name = name
		self.kill_count = 5#子弹伤害

	def kill(self,diren):
		pass
			


laowang = Person("老王")#创建老王
ak47 = Gun("ak47")#创建枪
danjia = DanJia("快速扩容",40)#创建弹夹

laowang.naqiang(gun)#让老王配枪

for i in range(40):#创建一些子弹
	zidan = ZiDan()
	laowang.zhuangzidan(danjia,zidan)

laowang.zhuangdanjia(ak47,danjia)#装弹夹

