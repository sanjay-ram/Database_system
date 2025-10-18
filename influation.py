import pandas as pd
import zipfile
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

with zipfile.ZipFile("API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_23195.zip", "r") as z:
    csv_name = [f for f in z.namelist() if f.startswith("API_") and f.endswith(".csv")][0]
    df = pd.read_csv(z.open(csv_name), skiprows=4)

switzerland = df[df["Country Name"] == "Switzerland"]

data = switzerland.melt(
    id_vars=["Country Name", "Country Code", "Indicator Name"],
    var_name="Year", value_name="Inflation"
)
data = data[data["Year"].str.isnumeric()]
data["Year"] = data["Year"].astype(int)
data = data[["Year", "Inflation"]].dropna()

X = data[["Year"]]
y = data["Inflation"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

X_all = np.arange(data["Year"].min(), 2031).reshape(-1, 1)
y_all_pred = model.predict(X_all)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse:.3f}")
print(f"R²: {r2:.3f}")

infl_2026 = model.predict(np.array([[2029]]))[0]
infl_2030 = model.predict(np.array([[2030]]))[0]

change_pct = ((infl_2030 - infl_2026) / abs(infl_2026)) * 100

print(f"Vorhergesagte Inflation 2029: {infl_2026:.2f}%")
print(f"Vorhergesagte Inflation 2030: {infl_2030:.2f}%")
print(f"Gesamtänderung 2029–2030: {change_pct:.2f}%")

plt.plot(data["Year"], data["Inflation"], color='blue', label='Tatsächliche Daten')
plt.plot(X_all, y_all_pred, color='red', linestyle='--', label='Vorhersage (Trendlinie)')
plt.xlabel("Jahr")
plt.ylabel("Inflation (%)")
plt.title("Inflation in der Schweiz – Lineare Trendlinie")
plt.legend()
plt.grid(True)
plt.show()
