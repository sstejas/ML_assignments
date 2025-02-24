import pandas as pd
import numpy as np

data=pd.read_excel("assig03.xlsx")
classA = data[data["Kidhome"]==0]
classB = data[data["Kidhome"]==1]
numeric_data = ["Recency","MntWines","MntFruits","MntMeatProducts","MntFishProducts"]
classA_mean = np.mean(classA[numeric_data],axis=0)
classB_mean = np.mean(classB[numeric_data],axis=0)

classA_std = np.std(classA[numeric_data],axis=0)
classB_std = np.std(classB[numeric_data],axis=0)

inter_dist = np.linalg.norm(classA_mean - classB_mean)

print("The intraclass distance of class A : ",classA_std)
print("The intraclass distance of class B : ",classB_std)
print("The interdistabce between A and B : ",inter_dist)
