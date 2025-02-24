import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report

data = pd.read_excel("assig03.xlsx")

numeric_data = ["Recency","MntWines","MntFruits","MntMeatProducts","MntFishProducts"]

X = data[numeric_data]
y = data["Kidhome"]

#A4
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

#A5
neigh = KNeighborsClassifier(n_neighbors=3) 
neigh.fit(X, y) 

#A6
accuracy = neigh.score(X_test,y_test)
print("The accuracy is : ",accuracy)


#A7
y_predict  = neigh.predict(X_test)
print("The predicted data is : ",y_predict[:5])
print("The original data is : ",y_test[:5])

#A8

accuracy_score = []
k_list = list(range(1,12))

for i in k_list:
    neighT = KNeighborsClassifier(n_neighbors=i)
    neighT.fit(X,y)
    score = neighT.score(X_test,y_test)
    accuracy_score.append(score)

plt.plot(k_list,accuracy_score,'o-')
plt.show()    

#A9
y_train_pred = neigh.predict(X_train)
y_test_pred = neigh.predict(X_test)
conf_matrix_train = confusion_matrix(y_train, y_train_pred)
conf_matrix_test = confusion_matrix(y_test, y_test_pred)

report_train = classification_report(y_train, y_train_pred)
report_test = classification_report(y_test, y_test_pred)

print("Confusion Matrix - Training Data:")
print(conf_matrix_train)
print("\nClassification Report - Training Data:")
print(report_train)

print("Confusion Matrix - Test Data:")
print(conf_matrix_test)
print("\nClassification Report - Test Data:")
print(report_test)

