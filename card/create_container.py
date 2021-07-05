import dash_html_components as html
import dash_bootstrap_components as dbc

# Helper Functions
def create_card(datum):

    # DATUM CONTIANS:
    # 'displayName', 'logo', 'record', 'standingSummary', 'color', 'alternateColor'
    name = datum['displayName']
    logo = datum['logo']
    record = datum['record']
    summary = datum['standingSummary']
    color = datum['color']
    alt_color = datum['alternateColor']

    print(name, record, summary)

    card = dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H4(name, className="card-title"),

                                        html.P(f"Standing: {summary}", className="card-text")
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

                            className="upper-card-container"
                        )
                    ],

                    style=dict(
                        fontFamily="Frutiger, Frutiger Linotype, Univers, Calibri, Gill Sans, Gill Sans MT, Myriad Pro, Myriad,\
                            DejaVu Sans Condensed, Liberation Sans, Nimbus Sans L, Tahoma, Geneva, Helvetica Neue, \
                            Helvetica, Arial, sans-serif"
                    )
                ),
                dbc.CardFooter(f"{record}"),
            ],

            className='card-containers',
            style=dict(
                width="18rem",
                margin="5px"
            )
        )
    print(type(card))
    return card