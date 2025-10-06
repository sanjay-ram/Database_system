import pandas as pd
import dash
from dash import dcc, html
from sklearn.linear_model import LinearRegression
import numpy as np
import plotly.express as px

df = pd.read_csv('exams.csv')


def categorize_subject(name):
    name_lower = name.lower()
    if "mathe" in name_lower:
        return "Mathematik"
    elif "deutsch" in name_lower:
        return "Deutsch"
    elif "geschichte" in name_lower:
        return "Geschichte"
    else:
        return "Sonstiges"

df["Fach"] = df["name"].apply(categorize_subject)

app = dash.Dash(__name__)
figures = []
for fach in df["Fach"].unique():
    fach_df = df[df["Fach"] == fach].sort_values("solved")
    X= np.arange(len(fach_df)).reshape(-1, 1)
    y = fach_df["result"].values
    model = LinearRegression()
    model.fit(X, y)

    fig = px.line(fach_df, x="solved", y="result", title=f"Leistung im Fach {fach}", markers= True)
    figures.append(dcc.Graph(figure=fig))

app.layout = html.Div([
    html.H1("Prüfungsleistungen nach Fach"),
    *figures
])

if __name__ == '__main__':
    app.run(debug=True)