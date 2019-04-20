import math
import matplotlib.pyplot as plt 

def tup(x):
	return (x[1],x[0]) 

x = [2,4,4,4,6,6]
y = [4,6,4,2,4,2]
op = [0,0,1,0,0,1]
test = (6,6)

dist = {}
n = len(x)
for i in range(n):
	d = (x[i]-test[0])**2 + (y[i]-test[1])**2
	d = math.sqrt(d)
	dist[i] = d

dist = dist.items()

dist = sorted(dist,key = tup)

print(dist)

k=3
testop = []
for i in range(k):
	testop.append(op[dist[i][0]])
max = 0
for i in testop:
	if testop.count(i)>max:
		max = testop.count(i)
		maxval = i

print(maxval)
x0 = [2,4,4,6]
y0 = [4,6,2,4]
plt.scatter(x0,y0,color="orange")

x1 = [4,6]
y1 = [4,2]
plt.scatter(x1,y1,color="b")

xo = [6]
yo = [6]
if maxval ==0:
	plt.scatter(xo,yo,color = "orange")
else:
	plt.scatter(xo,yo,color = "b")
plt.show()
