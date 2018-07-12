class Person():#人类
	def __init__(self,name):
		self.name = name
		


class Gun():#枪类
	def __init__(self,name):
		self.name = name

class DanJia():#弹夹类
	def __init__(self,name,count):
		self.name = name
		self.count = count


class ZiDan():#子弹
	def __init__(self,name):
		self.name = name


laowang = Person("老王")
ak47 = Gun("ak47")
danjia = DanJia("快速扩容",40)

for i in range(40):
	zidan = ZiDan()

