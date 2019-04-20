import socket
import random

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 8978
host = '127.0.0.1'
s.connect((host,port))
m = s.recv(2048)
p,alpha,ka = m.split()
p = int(p)
alpha = int(alpha)
ka = int(ka)
b = int(random.random()*p)
kb = alpha**b%p

s.send(str(kb))
key = ka**b%p
print("Key is : "+str(key))