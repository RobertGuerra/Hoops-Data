import dash_html_components as html
import dash_bootstrap_components as dbc

def create_card(datum):

    # DATUM CONTIANS:
    # 'displayName', 'logo', 'record', 'standingSummary', 'color', 'alternateColor'
    name = datum['displayName']
    logo = datum['logo']
    record = datum['record']
    summary = datum['standingSummary']
    color = datum['color']
    alt_color = datum['alternateColor']

    className="first-place" if "1st" in record else "not-first"
    className="disp"
    className="image"

    print(name, record, summary,logo)

    card = dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H4(name, className="card-title", style={"display":"inline-table"}),
                                        #html.P(f"Standing: {summary}", className="disp"),
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
                        borderBottom="solid"
                    )
                ),
                dbc.CardFooter(
                    [
                        html.Div(
                            [
                                html.P(f"Season Record: {record}"),
                                html.P(f"Standing: {summary}", className="disp")
                            ]

                        ),
                    ],

                    style=dict(
                        display="flex",
                    )
                )
            ],

            className='card-containers',
            style=dict(
                width="18rem",
                margin="4px"
            ),
    )
    print(type(card))
    return card