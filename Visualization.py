import pandas as pd

# Load the data
df = pd.read_csv('nepse_cleaned.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Basic analysis
print(df.describe())
print(df.head())

# Time series analysis
df.set_index('Date', inplace=True)
returns = df['Daily_Return'].dropna()
print(f"Average Daily Return: {returns.mean():.4f}%")
print(f"Annual Volatility: {returns.std() * np.sqrt(252):.2f}%")

# Visualization
import matplotlib.pyplot as plt
plt.figure(figsize=(14, 6))
plt.plot(df.index, df['Close'])
plt.title('NEPSE Index 10-Year History')
plt.xlabel('Date')
plt.ylabel('Price (NPR)')
plt.show()