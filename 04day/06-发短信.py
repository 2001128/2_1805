class  Msg():


    def __sendMsg(self,money):#私有方法，不能直接调用
        if money > 0:
            print("发短信")
        else:
            print("余额不足")


    def sendMsg(self,money):#公有方法可以直接调用
        self.__sendMsg(money)#调用方法
msg = Msg()
msg.sendMsg(10)
