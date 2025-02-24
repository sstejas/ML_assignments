import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_excel("assig03.xlsx")
target = data["MntMeatProducts"]
print("The mean of the target is ",np.mean(target))
print("The standard deviation is : ",np.std(target))

plt.hist(target,bins = 10)
plt.show()