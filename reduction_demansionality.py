import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data =  {
    'AnnualIncome': [
        15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 
        20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 
        25, 25.5, 26, 26.5, 27, 27.5, 28, 28.5, 29, 29.5, 
        30, 30.5, 31, 31.5, 32, 32.5, 33, 33.5, 34, 34.5, 
        35,   # Normal points
        80, 85, 90  # Outliers
    ],
    'SpendingScore': [
        39, 42, 45, 48, 51, 54, 57, 60, 63, 66,
        69, 72, 75, 78, 81, 84, 87, 90, 93, 96,
        6, 9, 12, 15, 18, 21, 24, 27, 30, 33,
        5, 8, 11, 14, 17, 20, 23, 26, 29, 32,
        56,   
        2, 3, 100  
    ],
    'Age': [
        20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 
        25, 25.5, 26, 26.5, 27, 27.5, 28, 28.5, 29, 29.5, 
        30, 30.5, 31, 31.5, 32, 32.5, 33, 33.5, 34, 34.5, 
        35, 35.5, 36, 36.5, 37, 37.5, 38, 38.5, 39, 39.5, 
        40,   
        15, 60, 70  
    ]
}

df = pd.DataFrame(data)

print(df.head())

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df_scaled[:, 0], df_scaled[:, 1], df_scaled[:, 2], c='b', marker='o')

ax.set_xlabel('Annual Income (scaled)')
ax.set_ylabel('Spending Score (scaled)')
ax.set_zlabel('Age (scaled)')
plt.show()
# Dimensionality Reduction using PCA 

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df_scaled)
df_pca = pd.DataFrame(df_pca, columns=['PCA1', 'PCA2'])
print(df_pca.head())

plt.scatter(df_pca['PCA1'], df_pca['PCA2'], c='b', marker='o')
plt.title('PCA of Customer Data')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.show()
# Dimensionality Reduction using t-SNE

from sklearn.manifold import TSNE
tsne = TSNE(n_components=2, random_state=42)
df_tsne = tsne.fit_transform(df_scaled)
df_tsne = pd.DataFrame(df_tsne, columns=['t-SNE1', 't-SNE2'])
print(df_tsne.head())

plt.scatter(df_tsne['t-SNE1'], df_tsne['t-SNE2'], c='b', marker='o')
plt.title('t-SNE of Customer Data')
plt.xlabel('t-SNE1')
plt.ylabel('t-SNE2')
plt.show()