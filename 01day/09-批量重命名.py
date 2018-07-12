
import os
dir_name = input("请输入文件夹名字")

files = os.listdir(dir_name)
'''
1-珍藏版.py --- 1-珍藏版必属精品.py
'''

#os.chdir(dir_name)#改变到movies文件目录
#print(os.getcwd())
'''
for file in files:
    position = file.rfind(".")
    new_name = file[:position]+"必属精品"+file[position:]
    os.rename(file,new_name)
'''

for file in files:
    position = file.rfind(".")
    new_name = file[:position]+"必属精品"+file[position:]
    #movies/01-珍藏版.py
    #movies/01-珍藏版必属精品.py
    old_name = dir_name+"/"+file
    new_name = dir_name+"/"+new_name
    os.rename(old_name,new_name)
