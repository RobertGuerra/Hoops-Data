import dash_html_components as html
import pandas as pd


def create_children(home, away):
    home_ser = pd.Series(index=[list(d.keys())[0] for d in home], data=[list(d.values())[0] for d in home])
    away_ser = pd.Series(index=[list(d.keys())[0] for d in away], data=[list(d.values())[0] for d in away])

    home_div = html.Div(
        [
            html.H2(
                "HOME"
            ),

            html.P(
                "WINS: {}".format(home_ser['wins']),

            ),

            html.P(
                "LOSSES: {}".format(home_ser['losses'])
            )
        ],

        style={'width': '100%'}
    )

    away_div = html.Div(
        [
            html.H2(
                "AWAY"
            ),

            html.P(
                "WINS: {}".format(away_ser['wins']),

            ),

            html.P(
                "LOSSES: {}".format(away_ser['losses'])
            )
        ],

        style={'width': '100%'}
    )

    return [home_div, away_div]