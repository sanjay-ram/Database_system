import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path ="CHF_INR Historical Data.csv"
df = pd.read_csv(file_path)

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")
df["Year"] = df["Date"].dt.year

def PlotPolly(model, independent_variable, dependent_variable, name):
    x_new = np.linspace(min(independent_variable), max(independent_variable), 100)
    y_new = model(x_new)

    plt.figure(figsize=(10, 5))
    plt.scatter(independent_variable, dependent_variable, label="Echte Daten", color="blue")
    plt.plot(x_new, y_new, label="Polynomial Fit", color="red")

    plt.title("Exchange Rate CHF to INR")
    plt.xlabel(name)
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()

x = df["Year"]
y = df["Price"]
degree = 11
coefficients = np.polyfit(x, y, degree)
polynomial_model = np.poly1d(coefficients)
print(polynomial_model)
PlotPolly(polynomial_model, x, y, "Date of Year")
