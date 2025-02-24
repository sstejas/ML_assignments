import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.spatial.distance import minkowski

data = pd.read_excel("assig03.xlsx")

f1 = data["MntSweetProducts"]
f2 = data["MntMeatProducts"]

r_values = range(1, 11)
distances = [minkowski(f1, f2, r) for r in r_values]


plt.plot(r_values, distances, '-')
plt.show()
