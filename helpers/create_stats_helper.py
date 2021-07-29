import dash_html_components as html
import pandas as pd


import requests
import json
url = "https://content-api-prod.nba.com/public/1/draft/2021/board"

payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.5',
  'Referer': 'https://www.nba.com/',
  'Origin': 'https://www.nba.com',
  'DNT': '1',
  'Connection': 'keep-alive'
}


def create_stats(df):
    home = df["record"][0]['items'][0]['stats']
    print(home)
    home = [{d['name']: d['value']} for d in home]

    # away = df["record"][0]['items'][2]['stats']
    # away = [{d['name']: d['value']} for d in away]

    home_ser = pd.Series(index=[list(d.keys())[0] for d in home], data=[list(d.values())[0] for d in home])
    # away_ser = pd.Series(index=[list(d.keys())[0] for d in away], data=[list(d.values())[0] for d in away])
    print('printing...')
    print(home_ser)


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
                "Playoff_seed: {}".format(int(home_ser['playoffSeed']))
            ),
            html.P(
                "WINS: {}".format(int(home_ser['wins']))
            ),
            html.P(
                "LOSSES: {}".format(int(home_ser['losses']))
            ),
            html.P(
                "win%: {:.2%}".format((home_ser['winPercent']))
            ),
            html.P(
                "Games_behind: {}".format(int(home_ser['gamesBehind']))
            ),
            html.P(
                "Games_Played: {}".format(int(home_ser['gamesPlayed']))
            ),
            html.P(
                "Points_For: {}".format(int(home_ser['pointsFor']))
            ),
            html.P(
                "Points_Against: {}".format(int(home_ser['pointsAgainst']))
            ),
            html.P(
                "avg_Points_For: {}".format(int(home_ser['avgPointsFor']))
            ),
            html.P(
                "avg_Points_Against: {}".format(int(home_ser['avgPointsAgainst']))
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