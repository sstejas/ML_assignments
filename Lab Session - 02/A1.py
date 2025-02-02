import pandas as pd
import numpy as np

customer = pd.read_excel("customer.xlsx")

A = customer.iloc[:, 1:-1].values
C = customer.iloc[:, -1].values

dimensionality = A.shape[1]
num_vectors = A.shape[0]
rank_A = np.linalg.matrix_rank(A)
P_inverse = np.linalg.pinv(A)
print("Dimensionality of vector space: ",dimensionality)
print("Number of vectors: ", num_vectors)
print("Rank of Matrix A: ",rank_A)
print("The pseudo inverse is ",P_inverse)
