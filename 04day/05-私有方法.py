class Father():
        

    def __getAge(self):#私有方法
        return 40
    
    def getAge(self):#公有方法
        return self.__getAge()


f = Father()
#f.__getAge()
print(f.getAge())
