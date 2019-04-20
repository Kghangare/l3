import random
import math

def getGenerator(a,b,p):
	count = 0
	po =[]
	while True:
		x = random.randrange(p)
		rhs = (x**3 + a*(a**2) + b)%p
		if float(math.sqrt(rhs)).is_integer():
			po.append((x,int(math.sqrt(rhs))))
			count+=1
		if count ==2:
			break
	x1,y1 = po[0][0],po[0][1]
	x2,y2 = po[1][0],po[1][1]
	print("P1")
	print((x1,y1))
	print("P2")
	print((x2,y2))
	s = ((y2-y1)/(x2-x1))%p
	x3 = (s**2 -x1-x2)%p
	y3 = (s*(x1-x3)-y1)%p
	return (x3,y3)

print("Enter a prime number p:")
p = int(raw_input())

print("Enter the coeeficients a and b:")

while True:	
	a = int(raw_input())	
	b = int(raw_input())
	if (4*(a**3)+27*(b**2))%p==0:
		print("Invalid coefficients, try again")
	else:
		break
g = getGenerator(a,b,p)
print("Generator: "+str(g))
print("Enter the message to be sent(<p):")
msg = int(raw_input())

pa = 12
pb = 14
pubb = (g[0]*pb,g[1]*pb)

#encryption
k = random.randrange(p)
c1 = (k*g[0]+k*g[1])%p
c2 = (msg+pubb[0]*k+pubb[1]*k)%p
print("Ciphertext:")
print((c1,c2))
#decryption:
m = (c2 - pb*c1)%p
print("Message:")
print(m)