import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create sales data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [15000, 18000, 12000, 22000, 19000, 25000,
              28000, 24000, 20000, 30000, 27000, 35000],
    'Product': ['A', 'B', 'A', 'C', 'B', 'A',
                'C', 'B', 'A', 'C', 'B', 'A']
}

df = pd.DataFrame(data)

# Basic statistics
print("=== Sales Analysis ===")
print(f"Total Sales: {df['Sales'].sum()}")
print(f"Average Sales: {df['Sales'].mean()}")
print(f"Highest Sales: {df['Sales'].max()}")
print(f"Lowest Sales: {df['Sales'].min()}")

# Best month
best_month = df.loc[df['Sales'].idxmax(), 'Month']
print(f"Best Month: {best_month}")

# Chart
plt.figure(figsize=(10, 5))
plt.plot(df['Month'], df['Sales'], marker='o', color='blue')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()