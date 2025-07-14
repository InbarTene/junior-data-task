import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('purchases.csv')

# Clean the data
df.dropna(inplace=True)

# Group by category and sum amounts
summary = df.groupby('category')['amount'].sum().reset_index()

# Print summary
print("Total amount spent per category:")
print(summary)

# Plot
plt.figure(figsize=(8, 5))
plt.bar(summary['category'], summary['amount'], color='skyblue')
plt.title('Total Spend by Category')
plt.xlabel('Category')
plt.ylabel('Total Amount')
plt.tight_layout()
plt.savefig('category_spending.png')
plt.show()
