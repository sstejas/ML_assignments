import pandas as pd
import numpy as np


imputed_tyhroid = pd.read_csv("thyroid_Imputed_data.csv")
print(imputed_tyhroid.head())
columns_to_normalize = [20, 22, 24, 26, 28]
numric_cols = imputed_tyhroid.iloc[:,columns_to_normalize]
print(numric_cols)

for i in columns_to_normalize:
    col_min = imputed_tyhroid.iloc[:,i].min()
    col_max = imputed_tyhroid.iloc[:,i].max()
    imputed_tyhroid.iloc[:,i] = (imputed_tyhroid.iloc[:,i] - col_min) / (col_max - col_min)
    

print("Normalized data:")
print(imputed_tyhroid.iloc[:,columns_to_normalize].head())