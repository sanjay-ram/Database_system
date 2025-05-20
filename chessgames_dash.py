import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go

# Load the data
df = pd.read_csv('chessgames.csv')

opening_counts = df['Opening'].value_counts().reset_index()
opening_counts.columns = ['Opening', 'Count']


fig_express = px.pie(opening_counts, values='Count', names='Opening', title='Most Played Opening')
fig = go.Figure(data=[go.Pie(labels=opening_counts['Opening'], values=opening_counts['Count'], hole=0, textinfo='label+percent')])
fig.update_layout(title='Most Played Opening')

# Initialize the Dash app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Most Played Opening"),
    html.Div([
        html.H3("Plotly Express"),
        dcc.Graph(figure=fig_express)
    ], style={'width': '48%', 'display': 'inline-block', 'padding': '0 2%'}),
    html.Div([
        html.H3("Plotly Graph Objects"),
        dcc.Graph(figure=fig)
    ], style={'width': '48%', 'display': 'inline-block', 'padding': '0 2%'}),
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
