#Permutations for keys
p10 = [2,4,1,6,3,9,0,8,7,5]
p8 = [5,2,6,3,7,4,9,8]

#Permutations for Encryption
ip = [1,5,2,0,3,7,4,6]
fip = [3,0,2,4,6,1,7,5]

#Permutation in fk
fkp = [3,0,1,2,1,2,3,0]

#sboxes
s1 = [[1,0,3,2],
	  [3,2,1,0],
	  [0,2,1,3],
	  [3,1,3,2]]

s2 = [[0,1,2,3],
	  [2,0,1,3],
	  [3,0,1,0],
	  [2,1,0,3]]

#P4 permutation
p4 = [1,3,2,0]


def shift(key):
	l = key[:5]
	r = key[5:]
	res = l[1:]+l[0]+r[1:]+r[0]
	return res

def getPermutation(k,p):
	res = ''
	for i in range(len(p)):
		res += k[p[i]]
	return res

def getKeys(key):
	#P10 permutation of key
	p1 = getPermutation(key,p10)
	#left shift of key
	p1 = shift(p1)
	#get key1 from p8 permutation
	k1 = getPermutation(p1,p8)
	#2 left shifts of p1
	p1 = shift(p1)
	p1 = shift(p1)
	#get Key2 from p8 permutation
	k2 = getPermutation(p1,p8)
	return (k1,k2)

def addKey(r,k):
	p=''
	for i in range(len(r)):
		p += str(int(r[i])^int(k[i]))
	return p

def getSbox(l,sbox):
	row = int(l[0]+l[3],2)
	col = int(l[1]+l[2],2)
	n = sbox[row][col]
	return str(bin(n)[2:].zfill(2))

def fk(p,k):
	l,r = (p[:4],p[4:])
	r1 = getPermutation(r,fkp)
	r1 = getSbox(r1[:4],s1)+getSbox(r1[4:],s2)
	r1 = getPermutation(r1,p4)
	return addKey(r1,l)


def encrypt(p,key):
	#Generate Keys
	k1,k2 = getKeys(key)
	#initail Permutation
	p = getPermutation(p,ip)
	r1 = fk(p,k1)
	#switch
	bits = p[4:]+r1
	r2 = fk(bits,k2)
	return getPermutation(r2+r1,fip)
	
def decrypt(p,key):
	#Generate Keys
	k1,k2 = getKeys(key)
	#initail Permutation
	p = getPermutation(p,ip)
	r1 = fk(p,k2)
	#switch
	bits = p[4:]+r1
	r2 = fk(bits,k1)
	return getPermutation(r2+r1,fip)
	
print("Enter the plaintext to be encrypted:")
p = input()
print(len(p))
print("Enter the encryption key:")
key = input()
print(len(key))

c = encrypt(p,key)
print(c)
e = decrypt('10100010',key)
print(e)
