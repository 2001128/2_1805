class Tool:
    def copy():
        name = input("请输入备份的文件名字")
        new_name = input("请输入备份后的名字 需要后缀名")
        f = open(name,"r")
        
        f1 = open(new_name,"w")
        while True:
            if len(f.read()) == 0：
                break
            content = f.read(1024)
            f1.write(content)
            

        f.close()
        f1.close()

    def puliang():
        pass


    def writeContent():
        psss


    def readCotent():

        pass


def  mian():
    print("1.备份")
    print("2.重命名")
    print("3.写入")
    print("4.读取")
    num = int(input("请选择功能"))

    if num == 1:
        t =Tool()
        t.copy()
    elif num == 2:
        piliang()
    elif num == 3:
        writeContent()
    elif num == 4:
        readContent()


main()
