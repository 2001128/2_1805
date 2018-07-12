class A():
    
    def show(self):
        print("哈哈")



class B():
    
    def show1(self):
        print("呵呵")


class C(A,B):
    
    
    def show2(self):
        print("嘿嘿")


c = C()
c.show()
c.show1()
c.show2()
