import dash_html_components as html
import dash_bootstrap_components as dbc

def create_card(datum):
    name = datum['displayName']
    logo = datum['logo']
    record = datum['record']
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
            dbc.CardBody(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    dbc.CardImgOverlay(
                                        children=[
                                            html.Img(
                                                src=f"{logo}",
                                                className="image-logo"
                                            )
                                        ],
                                    ),

                                    html.H4(
                                        name,
                                        className="card-title",
                                        style=dict(
                                            display="inline-table",
                                            color="white",
                                            font="30px"
                                        )
                                    ),

                                    # html.Img(
                                    #     src=f"{logo}",
                                    #     className="image-logo",
                                    # ),
                                    html.Br(),
                                    html.P(f"Season Record: {record}"),
                                    html.P(f"Standing: {summary}",
                                           className=numberOne),
                                    html.A(html.Button(
                                        'Team Roster',
                                        className="card-button",
                                        style={"color":"white", "backgroundColor":"#" + team_color}),
                                        href=team_link, target='blank'
                                    ),
                                ],

                                className="title-date"
                            ),

                        ],
                        className="upper-card-container",
                    )
                ],
                style=dict(
                    backgroundColor="#" + team_color,
                )
            ),
        ],

        className='card',

    )

    return card
