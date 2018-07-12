class Father():

    def __init__(self):
        self.__count = 3#处过对象的个数

    def getCount(self):
        return self.__count

    def setCount(self,count):
        self.__count = count

f = Father()
#f.__count = 10
#print(f.__count)
f.setCount(20)
print(f.getCount())

