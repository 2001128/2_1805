from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.connect(("172.20.10.7",8080))

content = input("请输入内容:")

s.send(content.encode("gb2312"))
while True:
    msg = s.recv(1024)
    print(msg.decode("gb2312"))
