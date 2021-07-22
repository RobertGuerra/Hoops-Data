import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import pandas as pd

from dash.dependencies import Input, Output

from card.init_data import json_data
from helpers.create_stats_helper import create_stats
from app import app


layout = html.Div(
    [
        html.Div(
            [

            ],
            className="stats-title-container",
            id='stats-title-container'

        ),

        html.Div(

            className="stats-container",
            id="stats-container"
        )
    ],

    className="stats-page-layout"
)


@app.callback([Output('stats-title-container', 'children'),
               Output('stats-container', 'children')],
              [Input('url', 'pathname')])
def fetch_stats(pathname):
    name = pathname.split('/')[3].replace('%20', ' ')
    data = [datum for datum in json_data if datum["displayName"] == name]

    df = pd.DataFrame.from_records(data)

    stats_children = create_stats(df)

    team_color = df['color']

    title_children = [
        html.H1(
            name,
            className="stats-title",
            id='stats-title',
            style={
                'width': '100%',
                'font-size': '5em',
                'color': f'#{team_color[0]}',
                'text-shadow': '1px 1px 2px white'
            }
        ),
        html.A(
            dbc.Button(
                'HOME',
                className="home-button",
                style={'height': '3em', 'width': '8em', 'background-color': f'#{team_color[0]}', 'color': 'white'}
            ),
            href='/apps/start'
        )
    ]

    return title_children, stats_children




