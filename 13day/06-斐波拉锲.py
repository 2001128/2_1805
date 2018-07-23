i = 0
def test():
    a = 0
    b = 1
    while i <10:
        yield b
        a,b = b,a+b
t = test()
for i in t:
    print(i)
