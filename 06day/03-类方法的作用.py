class DateUtils():

    def __init__(self,y,m,d):
        self.y = y
        self.m = m
        self.d = d


    def outDate(self):
        print("今年是%s年%s月%s日"%(self.y,self.m,self.d))
    

    @classmethod
    def delDate(cls,date):
        y,m,d = date.split("-")
        #return y,m,d
        #return cls(y,m,d)
        return cls(y,m,d).outDate()




'''
今天2018年7月11号
'''
'''
y = 2018
m = 7
d = 11
du = DateUtils(y,m,d)
du.outDate()
'''

'''
str = "2018-7-11"
y,m,d = str.split("-")
du = DateUtils(y,m,d)
du.outDate()
'''

'''
str = "2018-7-11"
y,m,d = DateUtils.delDate(str)
du = DateUtils(y,m,d)
du.outDate()
'''

'''
str = "2018-7-11"
du = DateUtils.delDate(str)
du.outDate()
'''

'''
str = "2018-7-11"
DateUtils.delDate(str).outDate()
'''

str = "2018-7-11"
DateUtils.delDate(str)
