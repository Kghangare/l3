import socket
import random

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 8978
host = '127.0.0.1'

s.bind((host,port))
s.listen(1)

c,addr = s.accept()

print("Enter Value of p:")
p=int(input())
print("Enter Value of alpha:")
alpha=int(input())

a = int(random.random()*p)
ka = alpha**a%p
msg = str(p)+' '+str(alpha)+' '+str(ka)
c.send(msg)
print("Key sent")
kb = c.recv(2048)
kb = int(kb)
key = kb**a%p
print("Key is : "+str(key))