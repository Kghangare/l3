import matplotlib.pyplot as plt
import math

def EuclidDist(p,m):
	d = (p[0]-m[0])**2 + (p[1]-m[1])**2
	return math.sqrt(d)

def getDist(x):
	return x[1]

points = [(2,4),(4,2),(4,4),(4,6),(6,2),(6,4)]
op = [0,0,1,0,1,0]
test = (6,6)
dist = {}
for i in range(len(points)):
	dist[i] = EuclidDist(points[i],test)
dist = sorted(dist.items(),key = getDist)
k = 3
neighbours = []
weight = []
for i in range(k):
	neighbours.append(op[dist[i][0]])
	weight.append(1/dist[i][1])
print(weight)
s1 = 0
s0 = 0
for i in range(k):
	if(neighbours[i]==0):
		s0 += weight[i]
	elif neighbours[i] ==1:
		s1 += weight[i]
print("S0: "+str(s0))
print("S1: "+str(s1))
if s0>s1:
	print('0')
	plt.scatter([6],[6],color = 'orange')
else:
	print('1')
	plt.scatter([6],[6],color = 'b')

p = [points[2],points[4]]
x = []
y = []
for i in range(len(p)):
	x.append(p[i][0])
	y.append(p[i][1])
plt.scatter(x,y,color = 'b')

p = [points[0],points[1],points[3],points[5]]
x = []
y = []
for i in range(len(p)):
	x.append(p[i][0])
	y.append(p[i][1])
plt.scatter(x,y,color = 'orange')
plt.show()