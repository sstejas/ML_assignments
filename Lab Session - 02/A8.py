import numpy as np
import pandas as pd

thyroid_data = pd.read_csv("thyroid_Imputed_data.csv")
binary_features = ['on thyroxine', 'query on thyroxine', 'on antithyroid medication', 'sick', 
                   'pregnant', 'thyroid surgery', 'I131 treatment', 'query hypothyroid', 
                   'query hyperthyroid', 'lithium', 'goitre', 'tumor', 'hypopituitary', 'psych']


thyroid_data[binary_features] = thyroid_data[binary_features].replace({'t': 1, 'f': 0})


vector_one = thyroid_data.iloc[0][binary_features].values
vector_two = thyroid_data.iloc[1][binary_features].values

def compute_similarity_metrics(arr1, arr2):
    match_11 = np.sum((arr1 == 1) & (arr2 == 1))  
    match_00 = np.sum((arr1 == 0) & (arr2 == 0)) 
    mismatch_10 = np.sum((arr1 == 1) & (arr2 == 0))
    mismatch_01 = np.sum((arr1 == 0) & (arr2 == 1)) 
    
    total_pairs = match_11 + match_00 + mismatch_10 + mismatch_01
    smc_value = (match_11 + match_00) / total_pairs if total_pairs != 0 else 0
    jc_value = match_11 / (match_11 + mismatch_10 + mismatch_01) if (match_11 + mismatch_10 + mismatch_01) != 0 else 0
    return smc_value, jc_value, match_11, mismatch_10, mismatch_01, match_00

smc_result, jc_result, count_11, count_10, count_01, count_00 = compute_similarity_metrics(vector_one, vector_two)


print(f"(1,1) Matches: {count_11}")
print(f"(1,0) Mismatches: {count_10}")
print(f"(0,1) Mismatches: {count_01}")
print(f"(0,0) Matches: {count_00}")
print(f"Simple Matching Coefficient (SMC): {smc_result}")
print(f"Jaccard Coefficient (JC): {jc_result}")