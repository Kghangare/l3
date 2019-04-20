import numpy as np 
import pandas as pd 
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score

from sklearn.model_selection import train_test_split 

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

from sklearn.preprocessing import LabelEncoder 
 
from IPython.display import Image  

import pydotplus 

data = pd.read_csv('Assignment2.csv')
print(data)

le = LabelEncoder()
data["Marital Status"] = le.fit_transform(data["Marital Status"])
data["Gender"] = le.fit_transform(data["Gender"])
data["Income"] = le.fit_transform(data["Income"])
data["Age"] = le.fit_transform(data["Age"])
print(data)
X = data.values[:, 1:5] 
Y = data.values[:, 5]

print(X)
print(Y)

print ("Dataset Length: ", len(data)) 
print ("Dataset Shape: ", data.shape)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 10)

clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100, max_depth = 3, min_samples_leaf = 5)

clf_entropy.fit(X_train,Y_train)

print("Results Using Entropy:\n")

Y_pred = clf_entropy.predict(X_test) 
print("Predicted values:") 
print(Y_pred)

print("Confusion Matrix: ", confusion_matrix(Y_test, Y_pred)) 
	
print ("Accuracy : ", accuracy_score(Y_test, Y_pred)*100) 


featureColumns = ['Age','Income','Gender','Marital Status']

dot_data = export_graphviz(clf_entropy, out_file=None, filled=True, rounded=True, special_characters=True, feature_names=featureColumns, class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data) 

graph.write_png('somefile.png')

Image(graph.create_png())

