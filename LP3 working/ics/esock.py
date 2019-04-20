import math
import random

print("Enter a number p:")
p = int(input())

#get parameters a and b
print("Enter the parameters a and b:")
while True:
	
	a=int(input())
	b=int(input())
	if (4*(a**3)+27*(b**2))%p!=0:
		break
	else:
		print("Invalid parameters, please enter again!")

#find generator point
x=0
while True:
	rhs = (x**3) + a*x + b
	y = math.sqrt(rhs)
	if y.is_integer():
		break
	x+=1
gen = (x,y)

#Assigning private keys of Alice and Bob
pra = 11
prb = 13

#Assigning public keys of Alice and Bob
puba = (pra*gen[0],pra*gen[1])
pubb = (prb*gen[0],prb*gen[1])

k = int(random.random()*p)

m=7
c1 = int(k*gen[0]+k*gen[1])%p
c2 = int(m+k*pubb[0]+k*pubb[1])%p
print("Ciphertext: "+str((c1,c2)))

m = int(c2 - prb*c1)%p
print("Decrypted text: "+str(m))
