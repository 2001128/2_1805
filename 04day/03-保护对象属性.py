class Dog():

    def __init__(self):
        self.__age = 1#私有属性


    def getAge(self):
        return self.__age
    
    def setAge(self,age):
        self.__age = age

dog = Dog()
#dog.__age = 20#这个属性就是__age
#print(dog.__age)

dog.setAge(10)
print(dog.getAge())
