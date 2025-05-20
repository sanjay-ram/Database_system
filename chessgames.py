import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('chessgames.csv')
values = df['Opening'].value_counts()
opening = np.array(values.index)
amount = np.array(values.values)

plt.figure(figsize = (11, 8))
plt.pie(amount, labels = opening, autopct='%1.1f%%')
plt.title("Most played Openings")
plt.show()