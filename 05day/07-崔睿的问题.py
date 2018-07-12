class A():
    def __init__(self):
        self.name = "老王"
        self.__age = 12

    def getAge(self):
        return self.__age

class B():
      
    def __init__(self):
        self.name = "老宋"

class C(A,B):
    def __init__(self):
        self.name = "老赵"

c = C()
print(c.name)
c.getAge()
 
