import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from card.init_data import card_data
from card.create_container import create_card


# app start
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div(
    html.Div(
        [
            dbc.Row(
                [
                    create_card(datum)

                    for datum in card_data
                ],

                style=dict(
                    display="flex",
                    justifyContent="left",
                    marginLeft="3.30%"
                )
            )
        ],

        id="card-output"
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)