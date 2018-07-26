from socket import * 

s = socket(AF_INET,SOCK_STREAM)

s.bind(("",6688))
print("----1----")
s.listen(5)#监听最大客户端连接数
print("----2----")
client,address = s.accept()
print("----3----")
msg = client.recv(1024)

print(msg.decode("gb2312"))

client.send("哈哈".encode("gb2312"))

client.close()#关闭

s.close()
