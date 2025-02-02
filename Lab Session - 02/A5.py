
import pandas as pd

df = pd.read_excel("thyroid.xlsx")
print(df.describe())

cata_column = df.select_dtypes(include=['object']).columns
print("Categorical columns:", cata_column)

ordinal_map = {"other": 0, "SVI": 1, "SVHC": 2, "SVHD": 3, "STMW": 4}
df["referral source"] = df["referral source"].map(ordinal_map)

df = pd.get_dummies(df, drop_first=True)

numeric_data = df.select_dtypes(include=['int64', 'float64'])
print("Min(or)Max values numeric columns:")
print(numeric_data.agg(['min', 'max']))

print("Missing values per column:")
print(df.isnull().sum())

print("Mean :", numeric_data.mean())
print("Variance :", numeric_data.var())
print("Standard deviation :", numeric_data.std())