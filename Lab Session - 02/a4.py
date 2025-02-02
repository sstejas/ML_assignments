import pandas as pd
import statistics
import matplotlib.pyplot as plt

file_path = 'Book1.xlsx'
df = pd.read_excel(file_path)

df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Chg%'] = pd.to_numeric(df['Chg%'], errors='coerce')

mean_price = statistics.mean(df['Price'].dropna())
variance_price = statistics.variance(df['Price'].dropna())

print(f"Mean Price: {mean_price}")
print(f"Variance of Price: {variance_price}")

wednesday_prices = df[df['Day'] == 'Wed']['Price'].dropna()
mean_wednesday_price = statistics.mean(wednesday_prices)

print(f"Mean Price on Wednesdays: {mean_wednesday_price}")
print(f"Difference from Population Mean: {mean_wednesday_price - mean_price}")

april_prices = df[df['Month'] == 'Apr']['Price'].dropna()
mean_april_price = statistics.mean(april_prices)

print(f"Mean Price in April: {mean_april_price}")
print(f"Difference from Population Mean: {mean_april_price - mean_price}")

total_days = len(df['Chg%'].dropna())
loss_days = len(df[df['Chg%'] < 0])
prob_loss = loss_days / total_days

print(f"Probability of ma a loss: {prob_loss:.2%}")

wednesday_data = df[df['Day'] == 'Wed']
wednesday_profit_days = len(wednesday_data[wednesday_data['Chg%'] > 0])
prob_profit_wed = wednesday_profit_days / len(wednesday_data)

print(f"Probability profit on Wednesday: {prob_profit_wed:.2%}")

print(f"Conditional probability of Wednesday: {prob_profit_wed:.2%}")

plt.figure(figsize=(10, 6))
plt.scatter(df['Day'], df['Chg%'], color='blue')
plt.title('Change % vs Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Change %')
plt.show()
