import dash
import dash_html_components as html
from dash.dependencies import Input, Output

from card.init_data import json_data
from card.create_container import create_card

from helpers.sort_cards_helper import sort_cards
from helpers.components.navbar_helper import Navbar

# app start init
from app import app


layout = html.Div(
    children=[
        Navbar(),

        html.Div(
            [
                create_card(datum)

                for datum in json_data
            ],

            id="card-output",
            className="card-grid"
        )
    ],

    className="outermost-div"
)

@app.callback(
    [Output("card-output", "children"),
     Output("team-list", "label")],
    [Input(option, "n_clicks") for option in
     sorted(["All Teams", "Atlantic", "Southeast", "Central", "Northwest", "Pacific", "Southwest"])]
)
def update_cards(*args):
    ctx = dash.callback_context

    if not ctx.triggered:
        division = "All Teams"
    else:
        division = ctx.triggered[0]["prop_id"].split(".")[0]

    if division == "All Teams":
        return [create_card(datum) for datum in json_data], division

    # sort_cards: helper function from sort_cards_helper
    sorted_team_data = sort_cards(json_data, division)

    division_list = [ create_card(datum) for datum in sorted_team_data ]

    return division_list, division

