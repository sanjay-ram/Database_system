import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



filename = "beste_doener.csv"
df = pd.read_csv(filename)
values = df['Ort'].value_counts()
orte = np.array(values.index)
amount = np.array(values.values)

plt.figure(figsize=(11, 8))
plt.pie(amount, labels=orte, autopct='%1.1f%%')
plt.title("Der beste Döner")
plt.show()