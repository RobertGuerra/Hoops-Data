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
    about_cards = dbc.Card(
        html.A(
            dbc.CardBody(
                [
                    html.H1("Robert James Guerra", style={"fontSize":"1rem"})
                ],
                style={"textAlignLast": "left"}
            ),
            href="https://github.com/RobertJG17"
        )
    )

    return about_cards


