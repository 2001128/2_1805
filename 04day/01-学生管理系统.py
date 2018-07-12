class Student():#学生类
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
        #属性
    
    def upClass(self):
        print("听课")
    
    def __str__(self):
        return "我的名字是%s我的性别是%s"%(self.name,self.sex)

class Manager():#管理类
    '''
    增删改查
    '''
    def __init__(self):
        self.list = []#装学生

    def add(self,student):
        self.list.append(student)
        for i in self.list:
            print(i)

    def remove(self):
        pass

    def update(self):
        pass

    def find(self):
        pass

class Menu():#菜单类
    
    def __init__(self):
        self.m = Manager()#让菜单持有管理类对象的引用

    def print_men(self):
        print("欢迎来学生管理系统")
        while True:
            fun = int(input("请选择功能"))
            if fun == 1:
                name = input("请输入学生名字")
                sex = input("请输入学生性别")
                s = Student(name,sex)
                self.m.add(s)# m = Manager()  m.add()
    
        
#m = Manager()
#name = input("请输入名字")
#s = Student(name)
#m.add(s)

m = Menu()
m.print_men()
'''
把输入写入文件
下次读出来出来
'''
