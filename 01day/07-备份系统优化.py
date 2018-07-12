name = input("请输入要备份的文件名字")
f = open(name,"r")

position = name.rfind(".")
newname = name[:position]+"back"+name[position:]
f1 = open(newname,"w")

while True:
    content = f.read(1024)#不能全部一下读取，根据字符读或者根据行读
    f1.write(content)
    if content == "": #len(content) == 0
        break

f.close()
f1.close()
'''
4.txt---4back.txt
1.txt---1back.txt
1234.txt =  1234   .txt
1234+back+.txt = 1234back.txt
字符串切片
find 
rfind()
'''

