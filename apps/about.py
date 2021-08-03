import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app

layout = html.Div(
    id='about-layout'
)


@app.callback(Output('about-layout', 'children'),
              [Input('url', 'pathname')])
def about_section(*args):

    about_cards = [

        html.Div(
            html.A(
                dbc.Button(
                    'HOME',
                    className="home-button",
                    style={'height': '3em', 'width': '8em', 'background-color': 'blue', 'color': 'white'}
                ),
                href='/apps/start',
                style={"margin": "auto", "textAlign": "center", "align-items": "baseline",
                       "textDecoration": "none", "display": "center"}
            ),
            style={"justifyContent": "center", "display": "flex"}
        ),
        html.Div(
                dbc.Card(
                    [
                        dbc.CardImg(
                            src="../assets/Bobby_git.png", top=True, bottom=False
                        ),
                            html.A(
                            dbc.CardBody(
                                [
                                    html.H1("Robert James Guerra",
                                    className='nba',
                                    style={"fontSize": "3rem"})
                                ],
                                style={"textAlignLast": "center"}
                            ),
                                style={"textDecoration": "none", "margin":"auto"},
                                href="https://github.com/RobertJG17",
                                target="blank"
                        )
                    ],
                ),
        ),
        html.Div(
            dbc.Card(
                [
                    dbc.CardImg(
                            src="../assets/rob_git.png", top=True, bottom=False
                        ),
                    html.A(
                        dbc.CardBody(
                            [
                                html.H1("Roberto Guerra",
                                className='nba',
                                style={"fontSize": "3rem"})
                            ],
                            style={"textAlignLast": "center"},
                        ),
                        style={"textDecoration": "none", "color":"blue", "margin":"auto"},
                        href="https://github.com/RobertGuerra",
                        target="blank"
                    ),

                ],
            ),
        )

    ]

    return about_cards


