import socket


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 9856
s.connect(('127.0.0.1',port))

m = s.recv(2048)
e,n = m.split()
e = int(e)
n = int(n)
print('Enter the message to be sent')
a = raw_input()
msg = []
for i in a:
	msg.append((ord(i)**e)%n)
a = ''
for i in range(len(msg)):
	if i == len(a)-1:
		a += str(msg[i])
	else:
		a += str(msg[i])+' '

s.send(a)
s.close()