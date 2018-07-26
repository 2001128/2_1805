from socket import *

s = socket(AF_INET,SOCK_DGRAM)

s.bind(("",8889))

s.sendto("李二蛋".encode("gb2312"),("172.20.10.7",8080))

while True:
    msg = s.recvfrom(1024)
    print("消息是:%s 来自ip:%s"%(msg[0].decode("gb2312"),msg[1][0]))

s.close()
