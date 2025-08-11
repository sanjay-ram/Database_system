import pandas as pd
import dash
from dash import dcc, html
from sklearn.linear_model import LinearRegression
import numpy as np
df = pd.read_excel('EU-CDT-extended_1.1-2.xlsx')


import plotly.express as px

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
hacking_count = df['Year'].value_counts().reset_index()
hacking_count.columns = ['Year', 'Count']
hacking_count = hacking_count.sort_values('Year')
X = hacking_count[['Year']]
y = hacking_count['Count']
model = LinearRegression().fit(X, y)

future_years = pd.DataFrame({'Year': np.arange(2024, 2028)})
future_years['Count'] = model.predict(future_years[['Year']])

combined = pd.concat([hacking_count, future_years], ignore_index=True)
fig = px.line(hacking_count, x='Year', y='Count', title="Cyberattacken in den letzten Jahren und Prognose")
fig.add_scatter(x=future_years['Year'], y=future_years['Count'], mode='lines+markers', name='Prognose', line=dict(dash='dash'))


app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Line-Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)
