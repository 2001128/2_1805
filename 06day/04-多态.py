class Animal(object):
    def eat(self):
        print("吃")

class Dog(Animal):
    def eat(self):
        print("狗粮")


class xtq(Dog):
    def eat(self):
        print("吃二氧化氮")

def eat_thing(dog):
    dog.eat()


shapi = Dog()
x = xtq()


eat_thing(shapi)
eat_thing(x)

