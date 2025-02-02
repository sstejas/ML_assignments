import pandas as pd
import numpy as np


data = pd.read_excel("thyroid.xlsx")


data.replace('?', np.nan, inplace=True)


numeric_columns = [19, 21, 23, 25, 27, 29]
data_numeric= data.iloc[:, numeric_columns].apply(pd.to_numeric, errors='coerce')


for col in data.columns:
    if data[col].dtype == 'object':
        
        data[col].fillna(data[col].mode()[0], inplace=True)
    else:
        
        iqr = data[col].quantile(0.75) - data[col].quantile(0.25)
        impute_value = data[col].median() if iqr > 0 else data[col].mean()
        data[col].fillna(impute_value, inplace=True)


print(data.head())


data.to_csv("thyroid_Imputed_data.csv", index=False)
