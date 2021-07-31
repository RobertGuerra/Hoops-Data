import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd


def create_bubble(title, info):
    return dbc.Card(
        dbc.CardBody(
            [
                html.H5(title, style={"text-align-last": "center"}),
                html.Hr(style={"backgroundColor": "white"}),
                html.P(round(info, 2), style={"text-align-last": "center"})
            ]
        ),

        style={"border-radius": "24px"}
    )


def create_stats(df):
    home = df["record"][0]['items'][0]['stats']
    home = [{d['name']: d['value']} for d in home]

    # away = df["record"][0]['items'][2]['stats']
    # away = [{d['name']: d['value']} for d in away]

    home_ser = pd.Series(index=[list(d.keys())[0] for d in home], data=[list(d.values())[0] for d in home])
    # away_ser = pd.Series(index=[list(d.keys())[0] for d in away], data=[list(d.values())[0] for d in away])



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

            html.Div(
                [
                    create_bubble(title="Playoff Seed", info=home_ser['playoffSeed']),
                    create_bubble(title="Wins", info=home_ser['wins']),
                    create_bubble(title="Losses", info=home_ser['losses']),
                    create_bubble(title="Win %", info=home_ser['winPercent']),
                    create_bubble(title="Games Behind", info=home_ser['gamesBehind']),
                    create_bubble(title="Games Played", info=home_ser['gamesPlayed']),
                    create_bubble(title="Points Scored", info=home_ser['pointsFor']),
                    create_bubble(title="Points Against", info=home_ser['pointsAgainst']),
                    create_bubble(title="Avg. Points Scored", info=home_ser['avgPointsFor']),
                    create_bubble(title="Avg. Points Against", info=home_ser['avgPointsAgainst']),
                    create_bubble(title="Division Win %", info=home_ser['divisionWinPercent']),
                    create_bubble(title="League Win %", info=home_ser['leagueWinPercent'])
                ],

                className="bubble-grid"
                # html.P(
                #     "Playoff_seed: {}".format(int(home_ser['playoffSeed']))
                # ),
                # html.P(
                #     "WINS: {}".format(int(home_ser['wins']))
                # ),
                # html.P(
                #     "LOSSES: {}".format(int(home_ser['losses']))
                # ),
                # html.P(
                #     "win%: {:.2%}".format((home_ser['winPercent']))
                # ),
                # html.P(
                #     "Games_behind: {}".format(int(home_ser['gamesBehind']))
                # ),
                # html.P(
                #     "Games_Played: {}".format(int(home_ser['gamesPlayed']))
                # ),
                # html.P(
                #     "Points_For: {}".format(int(home_ser['pointsFor']))
                # ),
                # html.P(
                #     "Points_Against: {}".format(int(home_ser['pointsAgainst']))
                # ),
                # html.P(
                #     "avg_Points_For: {}".format(int(home_ser['avgPointsFor']))
                # ),
                # html.P(
                #     "avg_Points_Against: {}".format(int(home_ser['avgPointsAgainst']))
                # ),
                # html.P(
                #     "division_Win_Percent: {:.2%}".format((home_ser['divisionWinPercent']))
                # ),
                # html.P(
                #     "league_Win_Percent: {:.2%}".format((home_ser['leagueWinPercent']))
                # )
            )
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