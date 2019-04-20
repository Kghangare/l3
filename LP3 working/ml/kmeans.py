import math
import matplotlib.pyplot as plt

points = [(0.1,0.6),(0.15,0.71),(0.08,0.9),(0.16,0.85),(0.2,0.3),
	 	  (0.25,0.5),(0.24,0.1),(0.3,0.2)]


m1 = points[0]
m2 = points[7]

c1=[]
c2=[]



itr = 0
while True:
	changed=0
	for p in points:
		d1 = math.sqrt((p[0]-m1[0])**2 + (p[1]-m1[1])**2)
		d2 = math.sqrt((p[0]-m2[0])**2 + (p[1]-m2[1])**2)
		if(d1<d2) and p in c2:
			c2.remove(p)
			c1.append(p)
			print('changed')
			changed=1
		elif d1>=d2 and p in c1:
			c1.remove(p)
			c2.append(p)
			changed=1
			print('changed')
		elif d1<d2 and p not in c1:
			c1.append(p)
			changed=1
			print('changed')
		elif d2<=d1 and p not in c2:
			c2.append(p)
			changed=1
			print('changed')
		
	(sx,sy)=(0,0)
	for p1 in c1:
		sx += p1[0]
		sy += p1[1]
	m1 = (sx/len(c1),sy/len(c1))

	(sx,sy)=(0,0)
	for p2 in c2:
		sx += p2[0]
		sy += p2[1]
	m2 = (sx/len(c2),sy/len(c2))
	itr+=1
	if changed ==0:
		break

print("Number of iterations: "+str(itr))
print("Cluster 1")
print(c1)
print(m1)

print("Cluster 2")
print(c2)
print(m2)

x=[]
y=[]
for i in c1:
	x.append(i[0])
	y.append(i[1])
plt.scatter(x,y,c='b')

x=[]
y=[]
for i in c2:
	x.append(i[0])
	y.append(i[1])
plt.scatter(x,y,c='r')

plt.show()
