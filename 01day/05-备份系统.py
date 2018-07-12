name = input("请输入要备份的文件名字")
f = open(name,"r")
content =  f.read()

'''
4.txt---4back.txt
1.txt---1back.txt
1234.txt =  1234   .txt
1234+back+.txt = 1234back.txt
字符串切片
find 
rfind()
'''
position = name.rfind(".")

newname = name[:position]+"back"+name[position:]

f1 = open(newname,"w")
f1.write(content)


f.close()
f1.close()
