import dash_html_components as html
import pandas as pd
import dash_core_components as dcc
from nba_lottery import get_lottery_picks
from dash.dependencies import Input, Output

def create_lotto_picks(lottery_df):
    home = lottery_df["record"][0]['items'][0]['stats']
    print(home)
    home = [{d['name']: d['value']} for d in home]

    # away = df["record"][0]['items'][2]['stats']
    # away = [{d['name']: d['value']} for d in away]

    home_ser = pd.Series(index=[list(d.keys())[0] for d in home], data=[list(d.values())[0] for d in home])
    # away_ser = pd.Series(index=[list(d.keys())[0] for d in away], data=[list(d.values())[0] for d in away])



    lottery_div = html.Div(
        [
            html.Hr(className="hr"),
            html.H2(
                "NBA LOTTERY",
                style={
                    "textAlignLast":"center"
                }
            ),

            html.Hr(className="hr"),

           dcc.Interval(
               id='my_interval',
               interval=1*3000,
           )
        ],

        style={'width': '100%'}
    )


    return [lottery_div]

