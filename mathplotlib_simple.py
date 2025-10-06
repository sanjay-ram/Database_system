from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('CHF_INR Historical Data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Change %'] = df['Change %'].str.replace('%', '').astype(float)

plt.plot (df['Year'], df['Change %'])
plt.xlabel(df['Year'])
plt.ylabel(df['Change %'])
plt.title("Change over Time")
plt.show()