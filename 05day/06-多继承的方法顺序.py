class A():
   
    def __init__(self):
        self.name = "老王"

    def show(self):
        print("哈哈")

class B():
    
    def __init__(self):
        self.name = "老宋"

    def show(self):
        print("呵呵")


class C(B,A):
    pass
    #def show(self):
     #   print("嘿嘿")


c = C()
c.show()
print(c.name)
print(C.__mro__)
