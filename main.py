import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import requests
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import json

response = requests.get('https://www.balldontlie.io/api/v1/stats')

print(response.text)

# Initialize Application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

balldontlie_df = pd.DataFrame.from_records(response.text)

def generateData(dataframe, col = 1000):
    data = json.loads(response.text)
    for i in data["data"]:
        print(i)



# main app layout
app.layout = html.Div([
    html.H1('Game Time!'),
    html.Div([
        html.H1(children='Player Data',
                className='table-heading'),

        html.Div([
            generateData(balldontlie_df)
            ])
        ]),
    ])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run_server(debug=True)