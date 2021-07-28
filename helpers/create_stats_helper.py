import dash_html_components as html
import pandas as pd
import dash_table
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from card.init_data import json_data
from IPython.display import display_html

def create_stats(df):
    home = df["record"][0]['items'][0]['stats']
    home = [{d['name']: d['value']} for d in home]

    away = df["record"][0]['items'][2]['stats']
    away = [{d['name']: d['value']} for d in away]

    home_ser = pd.Series(index=[list(d.keys())[0] for d in home], data=[list(d.values())[0] for d in home])
    away_ser = pd.Series(index=[list(d.keys())[0] for d in away], data=[list(d.values())[0] for d in away])

    # test_df = pd.DataFrame(home_ser)
    # my_dict = test_df.to_dict()

    home_div = html.Div(
        [
            html.Hr(className="hr"),
            html.H2(
                "Stats",
                style={
                    "textAlignLast":"center"
                }
            ),

            html.Hr(className="hr"),

            html.P(
                "Playoff_seed: {}".format(int(home_ser['playoffSeed'])),
            ),
            html.P(
                "WINS: {}".format(int(home_ser['wins'])),
            ),
            html.P(
                "LOSSES: {}".format(int(home_ser['losses']))
            ),
            html.P(
                "win%: {:.2%}".format((home_ser['winPercent'])),
            ),
            html.P(
                "Games_behind: {}".format(int(home_ser['gamesBehind'])),
            ),
            html.P(
                "Games_Played: {}".format(int(home_ser['gamesPlayed'])),
            ),
            html.P(
                "Points_For: {}".format(int(home_ser['pointsFor'])),
            ),
            html.P(
                "Points_Against: {}".format(int(home_ser['pointsAgainst'])),
            ),
            html.P(
                "avg_Points_For: {}".format(int(home_ser['avgPointsFor'])),
            ),
            html.P(
                "avg_Points_Against: {}".format(int(home_ser['avgPointsAgainst'])),
            ),
            html.P(
                "division_Win_Percent: {:.2%}".format((home_ser['divisionWinPercent']))
            ),
            html.P(
                "league_Win_Percent: {:.2%}".format((home_ser['leagueWinPercent']))
            ),
        ],

        style={'width': '100%'}
    )

    # away_div = html.Div(
    #     [
    #         html.Hr(className="hr"),
    #         html.H2(
    #             "AWAY"
    #         ),
    #         html.Hr(className="hr"),
    #
    #         html.P(
    #             "WINS: {}".format(int(away_ser['wins'])),
    #
    #         ),
    #
    #         html.P(
    #             "LOSSES: {}".format(int(away_ser['losses']))
    #         )
    #     ],
    #
    #     style={'width': '100%'}
    # )

    return [home_div]#, away_div]