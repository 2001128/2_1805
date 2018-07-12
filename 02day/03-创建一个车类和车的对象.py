class Car:


    def run(self):
        print("车在跑")

    def sing(self):
        print("在车里听音乐")

    def introduce(self):#self 谁调用这个方法就是指谁
        print("我是%s 我大小是%d 我的价格是%d"%(self.color,self.size,self.price))

    

bmw = Car()
bmw.run()
bmw.sing()

bmw.color = "红色"
bmw.size = 128
bmw.price = 1000000
bmw.introduce()


benchi = Car()
benchi.run()
benchi.sing()

benchi.color = "白色"
benchi.size = 100
benchi.price = 900000
benchi.introduce()




#print(bmw.color)
#print(bmw.size)
#print(bmw.price)
s
