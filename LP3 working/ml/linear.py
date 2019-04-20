import matplotlib.pyplot as plt

x = [10,9,2,15,10,16,11,16]
y = [95,80,10,50,45,98,38,93]

xm=0
ym=0
xy=0
xs=0
n=len(x)
for i in range(n):
	xm +=x[i]
	ym +=y[i]
	xy += x[i]*y[i]
	xs += x[i]*x[i]

xm = xm/n
ym = ym/n

b1 = (xy-n*xm*ym)/(xs-n*xm*xm)
b0 = ym-b1*xm

print("y = "+str(b1)+"x + "+str(b0))
plt.scatter(x,y)


y_pred = []
for i in range(n):
	y_pred.append(b1*x[i]+b0)
plt.plot(x,y_pred,color='r')
plt.xlabel('No. of hours spent driving')
plt.ylabel('Risk Score')
plt.show()