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

file_path= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
file_name = "usedcars.csv"

download(file_path, file_name)


df = pd.read_csv(file_name, header = 0)

df.head()
df_group_one = df[['body-style', 'price']]
df_grouped = df_group_one.groupby(['body-style', 'price'],as_index=False).mean()
print(df_grouped)