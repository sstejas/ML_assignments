import pandas as pd
import numpy as np
from numpy.linalg import pinv

file_path = "customer.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

A = df.iloc[:, 1:-1].values
C = df.iloc[:, -1].values.reshape(-1, 1)

P_inverse = pinv(A)
X_model = P_inverse @ C

print("the  vector X (predicted cost of the  product):")
print(X_model)