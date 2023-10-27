import pandas as pd
import matplotlib.pyplot as plt


file_path = ("C:/Users/Legion/Desktop/archive/SuperStore_Sales_Dataset.csv")
data = pd.read_csv(file_path)

# Total revenue for the month
total_revenue = data['Sales'].sum()

# Best selling product
most_sold_item = data['Customer Name'].value_counts().idxmax()

# Average price of goods
average_price = data['Sales'].mean()

# Grouping data by date and summarizing revenue
daily_revenue = data.groupby('Order Date')['Sales'].sum()

# Creating a graph
plt.figure(figsize=(10, 6))
daily_revenue.plot(kind='line')
plt.title('Change in revenue by days')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.grid(True)

plt.show()

print(f'Total revenue for the month: {total_revenue}')
print(f'Best selling product: {most_sold_item}')
print(f'Average price of goods: {average_price}')