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

    print(name, record, summary,logo)

    card = dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H4(name, className="card-title"),

                                        html.P(f"Standing: {summary}", className=className),

                                    ],

                                    className="title-date"
                                ),

                                # html.P(
                                #     error_text,
                                #     className="error-text",
                                #     hidden=is_valid,
                                #     style=dict(
                                #         marginLeft="60px",
                                #         fontWeight=100
                                #     )
                                # )

                            ],
                            className="upper-card-container",
                        )
                    ],

                    style=dict(
                        fontFamily="Frutiger, Frutiger Linotype, Univers, Calibri, Gill Sans, Gill Sans MT, Myriad Pro, Myriad,\
                            DejaVu Sans Condensed, Liberation Sans, Nimbus Sans L, Tahoma, Geneva, Helvetica Neue, \
                            Helvetica, Arial, sans-serif",
                    )
                ),
                dbc.CardFooter(
                    [
                        html.Div(
                            f"Season Record: {record}",
                            className=className,
                            style=dict(
                                display="flex",
                            )
                        ),

                        html.Div(
                            html.Img(
                                src=f"{logo}",
                                height="80%",
                                width="80%"
                            ),

                            style=dict(
                                marginLeft="50%"
                            )
                        )
                    ],

                    style=dict(
                        display="flex",

                    )
                               # style={
                               #     "backgroundImage":f"url({logo})",
                               #     "backgroundSize":"25% auto",
                               #     "backgroundRepeat":"no-repeat"
                               # }
                )
            ],

            className='card-containers',
            style=dict(
                width="18rem",
                margin="2px"
            ),
    )
    print(type(card))
    return card