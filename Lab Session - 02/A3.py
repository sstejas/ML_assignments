import pandas as pd
new_data = pd.read_excel("customer.xlsx")

for i in new_data.index:
    if new_data.loc[i,'Payment (Rs)'] > 200:
        new_data.loc[i,"Type"] = "Rich"
    else:
        new_data.loc[i,
                     "Type"] = "Poor"    

status= new_data[['Customer', 'Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)', 'Payment (Rs)', 'Type']]
print(status)