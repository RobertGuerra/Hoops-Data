import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from card.init_data import json_data
from card.create_container import create_card

from helpers.sort_cards_helper import sort_cards

# app start init
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY],
                meta_tags=[{
                    'name':'viewport',
                    'content':'width=device-width, initial-scale=1.0, maximum-scale-1.2, minimum-scale=0.5'}],
                suppress_callback_exceptions=True)


app.layout = html.Div(
    children=[
        dbc.NavbarSimple(
            children=[
                html.H1(
                    "TITLE HERE"
                ),


                dbc.DropdownMenu(
                    [
                        dbc.DropdownMenuItem(i, id=i)
                        for i in sorted(
                            ["All Teams", "Atlantic", "Southeast", "Central", "Northwest", "Pacific", "Southwest"]
                        )
                    ],
                    nav=True,
                    label="All Teams",
                    id="team-list",
                    in_navbar=True,
                    className="dropdown"
                )

            ],

            className="navbar",
            brand="NBA",
            brand_href = "https://www.nba.com/",
            brand_external_link="https://www.nba.com/",
            color="primary",
            sticky=True,
            dark=True
        ),

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

if __name__ == '__main__':
    app.run_server('0.0.0.0', 5000, debug=True)