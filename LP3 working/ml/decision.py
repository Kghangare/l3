import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import sklearn.metrics as mt

data = pd.read_csv('data.csv')
cols = list(data)
for i in cols:
	val = data[i]
	vals = list(set(val))
	for j in range(len(val)):
		data[i][j] = vals.index(data[i][j])

features = list(data)[:-1]
print(features)
X = data[features]
Y = data.Buys.astype('int')

Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,Y,test_size=0.3,random_state=1)

classifier = DecisionTreeClassifier()
classifier = classifier.fit(Xtrain,Ytrain)

Ypred = classifier.predict(Xtest)

print(mt.accuracy_score(Ytest,Ypred))


