import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load and clean the dataset
data = pd.read_csv("effects-of-covid-19-on-trade-at-15-december-2021-provisional 1.csv")
data.ffill(inplace=True)
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)

# Setting up the Dash application
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Effects of COVID-19 on Trade Analysis"),
    
    html.Label("Select a Country:"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in data['Country'].unique()],
        value=data['Country'].unique()[0]  # Default value
    ),
    
    dcc.Graph(id='trade-value-graph'),
])

@app.callback(
    Output('trade-value-graph', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    filtered_data = data[data['Country'] == selected_country]
    fig = px.line(
        filtered_data,
        x='Date',
        y='Value',
        title=f'Trade Value Over Time for {selected_country}',
        labels={'Value': 'Trade Value', 'Date': 'Date'}
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)