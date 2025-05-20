import pandas as pd
import dash
from dash import html, dcc

df = pd.read_csv('stastic_reading.csv')

import plotly.express as px

fig_express = px.pie(df, values='Bücher pro Jahr (ø) Regelmäßige Leser (%)', names='Generation', title = "Regelmässige Leser")
fig_express.show()

import plotly.graph_objects as go

fig = go.Figure(
    data_a = [go.Pie(labels = df['Generation'], values = df['Bücher pro Jahr (ø) Regelmäßige Leser (%)'], hole = 0, textinfo= 'label+percent')] )

fig.update_layout(title = "Regelmässige Leser (%)")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Regelmässige Leser"),
    html.Div([
        html.H3("plotly.express"),
        dcc.Graph(figure=fig_express),
    ], style={"width": "48%", "display": "inline-block", "padding": "0 2%"}),
    html.Div([
        html.H3("plotly.graph_objects"),
        dcc.Graph(figure=fig),
    ], style={"width": "48%", "display": "inline-block", "padding": "0 2%"})
])

if __name__ == '__main__':
    app.run_server(debug=True)