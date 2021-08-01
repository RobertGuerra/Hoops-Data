from dash.exceptions import PreventUpdate
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import pandas as pd

from dash.dependencies import Input, Output

from card.init_data import json_data

from app import app
import json

layout = html.Div(
    [
        html.Div(

            className="stats-title-container",
            id='stats-title-container'

        ),

        # html.Div(
        #
        #     className="stats-container",
        #     id="stats-container"
        # ),

        html.Div(
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
                            dbc.Tabs(
                                [
                                    dbc.Tab(label="Playoff Seed", tab_id="tab-1"),
                                    dbc.Tab(label="Wins", tab_id="tab-2"),
                                    dbc.Tab(label="Losses", tab_id="tab-3"),
                                    dbc.Tab(label="Win Percent", tab_id="tab-4"),
                                    dbc.Tab(label="Games Behind", tab_id="tab-5"),
                                    dbc.Tab(label="Games Played", tab_id="tab-6"),
                                    dbc.Tab(label="Points For", tab_id="tab-7"),
                                    dbc.Tab(label="Points Against", tab_id="tab-8"),
                                    dbc.Tab(label="Avg. Points For", tab_id="tab-9"),
                                    dbc.Tab(label="Avg. Points Against", tab_id="tab-10"),
                                    dbc.Tab(label="Division Win %", tab_id="tab-11"),
                                    dbc.Tab(label="League Win %", tab_id="tab-12")
                                ],
                                id="tabs",
                                className="stats-tabs",
                                active_tab="tab-1"
                            ),
                            html.Div(id="content"),
                        ]
                    )
            ]
        ),

        dcc.Store(
            id="callback-store"
        )
    ],

    className="stats-page-layout"
)


@app.callback([Output('stats-title-container', 'children'),
               Output('callback-store', 'data')],
              [Input('url', 'pathname')])
def fetch_stats(pathname):
    name = pathname.split('/')[3].replace('%20', ' ')
    data = [datum for datum in json_data if datum["displayName"] == name]


    df = pd.DataFrame.from_records(data)


    # stats_children = create_stats(df)


    team_color = df['color']
    team_link = df['team-link'].iloc[0]
    team_logos = df['logo']

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
            href='/apps/start',
            style={"margin": "auto"}
        ),
        html.A(
            html.Img(
                src=f"{team_logos[0]}",
                style={
                    "position": "relative",
                    "width": "11rem",
                    "height": "11rem",
                    "top":"5px"
                }
            ),
            href=team_link,
            target="blank",
            style={"margin": "auto"}
        ),
        html.P("Team Roster",
               style={"display":"relative"}
        ),
    ]

    data = json.dumps(df.to_json())


    return title_children, data

@app.callback(Output("content", "children"),
              [Input("callback-store", "data"),
               Input("tabs", "active_tab")])
def switch_tab(data, at):

    if data is None:
        raise PreventUpdate

    df = pd.read_json(json.loads(data))

    stats_rec = df["record"][0]['items'][0]['stats']
    stats_rec_formatted = [{d['name']: d['value']} for d in stats_rec]

    stats_ser = pd.Series(index=[list(d.keys())[0] for d in stats_rec_formatted],
                          data=[list(d.values())[0] for d in stats_rec_formatted])


    tab1_content = dbc.Card(
        dbc.CardBody(
            [
                html.H3("{}".format(int(stats_ser['playoffSeed'])))
            ],

            style = {"textAlignLast": "center"}
        )
        #className="mt-3",
    )

    tab2_content = dbc.Card(
        dbc.CardBody(
            [
                html.H3("{} Wins".format(int(stats_ser['wins'])))
            ],
            style={"textAlignLast":"center"}
        ),
    )
    tab3_content = dbc.Card(
        dbc.CardBody(
            [
                html.H3("{} Losses".format(int(stats_ser['losses'])))
            ],
            style={"textAlignLast": "center"}
        ),
    )
    tab4_content = dbc.Card(
        dbc.CardBody(
            [
                html.H3("{:.2%}".format(stats_ser['winPercent']))
            ],
            style={"textAlignLast": "center"}
        ),
    )
    tab5_content = dbc.Card(
        dbc.CardBody(
            [
                html.H3("{} Games".format(int(stats_ser['gamesBehind'])))
            ],
            style={"textAlignLast": "center"}
        ),
    )
    tab6_content = dbc.Card(
        dbc.CardBody(
            [
                html.H3("{} Games".format(int(stats_ser['gamesPlayed'])))
            ],
            style={"textAlignLast": "center"}
        ),
    )
    tab7_content = dbc.Card(
        dbc.CardBody(
            [
                html.H3("{} Points".format(int(stats_ser['pointsFor'])))
            ],
            style={"textAlignLast": "center"}
        ),
    )
    tab8_content = dbc.Card(
        dbc.CardBody(
            [
                html.H3("{} Points".format(int(stats_ser['pointsAgainst'])))
            ],
            style={"textAlignLast":"center"}
        ),
    ),
    tab9_content = dbc.Card(
        dbc.CardBody(
            [
                html.H3("{} Points".format(int(stats_ser['avgPointsFor'])))
            ],
            style={"textAlignLast": "center"}
        ),
    ),
    tab10_content = dbc.Card(
        dbc.CardBody(
            [
                html.H3("{} Points".format(int(stats_ser['avgPointsAgainst'])))
            ],
            style={"textAlignLast": "center"}
        ),
    ),
    tab11_content = dbc.Card(
        dbc.CardBody(
            [
                html.H3("{:.2%}".format(stats_ser['divisionWinPercent']))
            ],
            style={"textAlignLast": "center"}
        ),
    ),
    tab12_content = dbc.Card(
        dbc.CardBody(
            [
                html.H3("{:.2%}".format(stats_ser['leagueWinPercent']))
            ],
            style={"textAlignLast": "center"}
        ),
    ),



    if at == "tab-1":
        return tab1_content
    elif at == "tab-2":
        return tab2_content
    elif at == "tab-3":
        return tab3_content
    elif at == "tab-4":
        return tab4_content
    elif at == "tab-5":
        return tab5_content
    elif at == "tab-6":
        return tab6_content
    elif at == "tab-7":
        return tab7_content
    elif at == "tab-8":
        return tab8_content
    elif at == "tab-9":
        return tab9_content
    elif at == "tab-10":
        return tab10_content
    elif at == "tab-11":
        return tab11_content
    elif at == "tab-12":
        return tab12_content
    return html.P("This shouldn't ever be displayed...")



