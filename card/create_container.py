import dash_html_components as html
import dash_bootstrap_components as dbc


def create_card(datum):

    # DATUM CONTIANS:
    # 'displayName', 'logo', 'record', 'standingSummary', 'color', 'alternateColor'
    name = datum['displayName']
    logo = datum['logo']
    record = datum['record']
    summary = datum['standingSummary']
    team_color = datum['color']
    alt_color = datum['alternateColor']


    # fire for first place
    numberOne = "fire" if "1st" in datum['standingSummary'] else ''


    # give "white" to alt_color if it resembles team_color
    if alt_color.upper() == team_color.upper() or name in ["Los Angeles Lakers", "Memphis Grizzlies", "Indiana Pacers", "Oklahoma City Thunder", "Toronto Raptors"]:
        alt_color = "FFFFFF"


    card = dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H4(
                                            name,
                                            className="card-title",
                                            style=dict(
                                                display="inline-table",
                                                color="#" + team_color,
                                                textShadow="-0.4px 0.6px #" + alt_color,
                                                font="30px"
                                            )
                                        ),

                                        html.Img(
                                            src=f"{logo}",
                                            className="image-logo"
                                        ),
                                    ],

                                    className="title-date"
                                ),

                            ],
                            className="upper-card-container",
                        )
                    ],
                    style=dict(
                        fontFamily="Frutiger, Frutiger Linotype, Univers, Calibri, Gill Sans, Gill Sans MT, Myriad Pro, Myriad,\
                            DejaVu Sans Condensed, Liberation Sans, Nimbus Sans L, Tahoma, Geneva, Helvetica Neue, \
                            Helvetica, Arial, sans-serif",
                        #borderBottom="solid",
                        backgroundColor="dark-gray",
                        fontWeight="200"
                    )
                ),

                dbc.CardFooter(
                    [
                        html.Div(
                            [
                                html.P(f"Season Record: {record}"),
                                html.P(f"Standing: {summary}",
                                       className=numberOne)
                            ],
                        ),
                    ],

                    style=dict(
                        display="flex",
                        backgroundColor='#' + team_color,
                        justifyContent="center"
                    )
                )
            ],

            className='card-containers',
            style=dict(
                width="18rem",
                margin="4px",
                textAlign="-webkit-center",
            ),
    )

    return card