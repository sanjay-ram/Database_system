import matplotlib
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import seaborn as sns
# data science from sanjay
def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

filepath="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod2.csv"
file_name = "laptops.csv"
download(filepath, file_name)
df = pd.read_csv(file_name, header = 0)
df.head(5)
print(sns.regplot(x = 'CPU_frequency', y = 'Price', data = df),
      plt.ylim(0,))