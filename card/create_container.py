import dash_html_components as html
import dash_bootstrap_components as dbc

def create_card(datum):
    name = datum['displayName']
    logo = datum['logo']
    record = datum['record_ovr']
    summary = datum['standingSummary']
    team_color = datum['color']
    alt_color = datum['alternateColor']
    team_link = datum['team-link']

    # fire for first place
    numberOne = "fire" if "1st" in datum['standingSummary'] else ''

    # give "white" to alt_color if it resembles team_color
    # if alt_color.upper() == team_color.upper() or name in ["Los Angeles Lakers", "Memphis Grizzlies", "Indiana Pacers", "Oklahoma City Thunder", "Toronto Raptors"]:
    #     alt_color = "FFFFFF"

    if name in ["Toronto Raptors", "Houston Rockets"]:
        team_color = "000000"

    card = dbc.Card(
        [
            html.A(
                dbc.CardBody(
                    [
                        html.Div(
                            [
                                dbc.CardImgOverlay(
                                    children=[
                                        html.Img(
                                            src=f"{logo}",
                                            className="image-logo",
                                            style={
                                                # "opacity": ".4",
                                                "z-index": "0",
                                                "position": "relative",
                                                "padding-bottom":"10px"
                                            }
                                        )
                                    ],
                                ),

                                html.H4(
                                    name,
                                    className="card-title",
                                    style=dict(
                                        display="inline-table",
                                        color="white",
                                        font="30px",
                                        zIndex = "1",
                                        position = "relative"
                                    )
                                ),

                                # html.Img(
                                #     src=f"{logo}",
                                #     className="image-logo",
                                # ),
                                html.Br(),
                                html.B(f"Season Record: {record}",
                                       style={"z-index": "1", "position": "relative"}),
                                html.Br(),
                                html.B(f"Standing: {summary}",
                                       className=numberOne,
                                       style={"z-index": "1", "position": "relative"}),
                                # html.A(
                                #     html.Button(
                                #         'Team Roster',
                                #         className="card-button",
                                #         style={"color": "white", "backgroundColor": "#" + team_color}
                                #     ),
                                #     className="button-anchor",
                                #     href=team_link,
                                #     target='blank'
                                # ),
                            ],

                            className="title-date",
                        ),

                    ],

                    style=dict(
                        backgroundColor="#" + team_color,
                    )
                ),

                className="card-anchor",
                href="/apps/selected/{}".format(name)
            )
        ],

        className='team-card',

    )

    return card

