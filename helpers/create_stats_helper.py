import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import pandas as pd


def create_stats(df):
    home = df["record"][0]['items'][1]['stats']
    home = [{d['name']: d['value']} for d in home]

    away = df["record"][0]['items'][2]['stats']
    away = [{d['name']: d['value']} for d in away]

    home_ser = pd.Series(index=[list(d.keys())[0] for d in home], data=[list(d.values())[0] for d in home])
    away_ser = pd.Series(index=[list(d.keys())[0] for d in away], data=[list(d.values())[0] for d in away])

    home_div = html.Div(
        [
            html.Hr(className="hr"),
            html.H2(
                "HOME"
            ),
            html.Hr(className="hr"),

            html.P(
                "WINS: {}".format(int(home_ser['wins'])),

            ),

            html.P(
                "LOSSES: {}".format(int(home_ser['losses']))
            )
        ],

        style={'width': '100%'}
    )

    away_div = html.Div(
        [
            html.Hr(className="hr"),
            html.H2(
                "AWAY"
            ),
            html.Hr(className="hr"),

            html.P(
                "WINS: {}".format(int(away_ser['wins'])),

            ),

            html.P(
                "LOSSES: {}".format(int(away_ser['losses']))
            )
        ],

        style={'width': '100%'}
    )

    return [home_div, away_div]