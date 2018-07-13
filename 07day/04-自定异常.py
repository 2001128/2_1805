class ShowError(Exception):
    def __init__(self,name,least):
        self.name = name
        self.least = least
        
    def main():
        try:
            s = input("请输入一个名字:")
            if s == "老王":
                raiseShowError(name(s))
        except ShiwError as result:
            print("ShowError: 你输入的名字是%s 除%s外任何一个名字都可以")     
        #else:
         #   print("m")

main()
