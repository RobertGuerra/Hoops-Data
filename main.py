import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from card.init_data import card_data
from card.create_container import create_card

# app start
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])  #dbc.themes.DARKLY,  #dbc.themes.BOOTSTRAP

app.layout = html.Div(
            children=[
                html.Div(
                        [   # dropdown skeleton
                            dcc.Dropdown(
                                id='team-list',
                                options=[
                                    # {"label": i, "value": i}
                                    # for i in [card_data]
                                    {"label": "Eastern Conference", "value": 'NYC'},
                                    {"label": "Western Conference", "value": 'LA'},
                                    {"label": "Boston", "value": 'MA'}

                                ],

                                value=['LAL', 'BOS'],
                                placeholder="Selections",
                                multi=True
                            )
                        ],
                                style={
                                    "width": "25%",
                                    "margin-left": "475px",
                                    "margin-top":"10px",
                                    "margin-bottom":"10px",
                                    "verticalAlign":"middle",
                                    "color":"#000000"
                                }
                        ),
                    html.Div(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(create_card(datum), width=12, lg=3)
                                    for datum in card_data
                                    # create_card(datum)
                                    #
                                    # for datum in card_data
                                ],

                                style=dict(
                                    display="flex",
                                    justifyContent="left",
                                    #marginLeft="3.30%"
                                )
                            )
                        ],

                        id="card-output",
                    )
                ],
                # style={
                #     "margin":"auto"
                # }
            )
if __name__ == '__main__':
    app.run_server(debug=True)