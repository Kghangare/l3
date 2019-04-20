import socket

def gcd(a,b):
	r = a%b
	
	while(r):
		a=b
		b=r
		r=a%b
	return b

def getInverse(e,phin):
	dt = 0.0
	for i in range(1,phin):
		dt = (float(phin)*float(i)+1)/float(e)
		if dt.is_integer():
			return int(dt)
			 

def getKeys(p,q):
	n=p*q
	phin = (p-1)*(q-1)
	for i in range(2,phin):
		if(gcd(phin,i)==1):
			e=i
			break
	d = getInverse(e,phin)
	return (e,d)


if __name__ == "__main__":

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	port = 9856
	s.bind(('127.0.0.1',port))
	s.listen(1)
	c,addr = s.accept()

	print("Enter a prime p:")
	p = int(input())
	print("Enter a prime q:")
	q = int(input())
	n = p*q
	e,d=getKeys(p,q)

	c.send(str(e)+' '+str(n))
	cipher =c.recv(2048)
	c.close()
	msg = cipher.split()
	print(msg)
	print(d)
	m = ''
	for i in range(len(msg)):
		msg[i] = int(msg[i]) 
		m += chr((msg[i]**d)%n)
print("Message: "+m)

