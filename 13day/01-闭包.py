def test(a,b):
    def ads(x):
        return a*x+b
    
    return ads 

t = test(2,3)
print(t(2))
print(t(3))
print(t(4))



def test1(a,b,x):
    return a*x+b

print(test1(1,1,2))
print(test1(2,2,2))
