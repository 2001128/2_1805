import time
#写入操作

f = open("3.txt","w")
f.write("1807要修空调了")
f.close()
print("写入成功")
print("正在读取")

time.sleep(2)

#读取
f1 = open("3.txt","r")
content = f1.read()
print("读出来的内容是%s"%content)
