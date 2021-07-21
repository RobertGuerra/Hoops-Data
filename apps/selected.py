import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

from dash.dependencies import Input, Output

from card.init_data import json_data
from helpers.create_children import create_children
from app import app

data = []

layout = html.Div(
    [
        html.Div(
            html.H1(

                id='stats-title',
                style={'width': '100%'}
            ),

            className="stats-title-container",
        ),

        html.Div(

            className="stats-container",
            id="stats-container"
        )
    ],

    className="stats-page-layout"
)


@app.callback([Output('stats-container', 'children'),
               Output('stats-title', 'children')],
              [Input('url', 'pathname')])
def fetch_stats(pathname):
    name = pathname.split('/')[3].replace('%20', ' ')
    data = [datum for datum in json_data if datum["displayName"] == name]

    home_stats = pd.DataFrame.from_records(data)["record"][0]['items'][1]['stats']
    home_stats = [{d['name']: d['value']} for d in home_stats]

    away_stats = pd.DataFrame.from_records(data)["record"][0]['items'][2]['stats']
    away_stats = [{d['name']: d['value']} for d in away_stats]

    children = create_children(home_stats, away_stats)


    return children, name




