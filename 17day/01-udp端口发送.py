from socket import *
s = socket(AF_INET,SOCK_DGRAM)
s.sendto("李二蛋".encode("gb2312"),("172.20.10.7",6060))
s.close()
