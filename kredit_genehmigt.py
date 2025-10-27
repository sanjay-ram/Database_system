import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

df = pd.read_csv('C:\projects\Databasesystem\kreditdaten.csv')

print(df.head())

le = LabelEncoder()
df["Schulden"] = le.fit_transform(df["Schulden"])
df["Kredit_genehmigt"] = le.fit_transform(df["Kredit_genehmigt"])

X = df[["Alter", "Einkommen", "Kreditbetrag", "Schulden"]]
y = df["Kredit_genehmigt"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

print(f"Tree depth: {model.get_depth()}")
print(f"Number of leaves: {model.get_n_leaves()}")

y_pred = model.predict(X_test)
print(accuracy_score(y_test, y_pred))

plt.figure(figsize=(10, 6))
plot_tree(model, feature_names=X.columns, class_names=["Nein", "Ja"], filled=True)
plt.show()