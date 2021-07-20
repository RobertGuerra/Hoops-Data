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
                    'content':'width=device-width, initial-scale=1.0, maximum-scale-1.2, minimum-scale=0.5'}])


app.layout = html.Div(
    children=[
        html.Nav(
            dbc.NavbarSimple(
                children=[
                    dbc.NavItem(
                        dcc.Dropdown(
                            id="team-list",
                            options=[
                                {"label": i, "value": i}
                                for i in sorted(
                                    ["All Teams", "Atlantic", "Southeast", "Central", "Northwest", "Pacific", "Southwest"])

                            ],

                            className="dropdown",
                        )
                    )
                    # dcc.Dropdown(
                    #     id="team-list",
                    #     options=[
                    #         {"label": i, "value": i}
                    #         for i in sorted(
                    #             ["All Teams", "Atlantic", "Southeast", "Central", "Northwest", "Pacific", "Southwest"])
                    #
                    #     ],
                    #
                    #     className="dropdown",
                    # )
                ],
            brand="NBA",
            #brand_href = "https://www.nba.com/",
            brand_external_link="https://www.nba.com/",
            color="primary",
            dark=True,
            style={
                "position": "fixed",
                "left":"0",
                "top": "0",                 # /* Position the navbar at the top of the page */
                "width": "100%"             # /* Full width */
        }
    )
        ),
        # html.Div(
        #     [   # dropdown skeleton
        #         dcc.Dropdown(
        #             id="team-list",
        #             options=[
        #                 {"label": i, "value": i}
        #                 for i in sorted(["All Teams", "Atlantic", "Southeast", "Central", "Northwest", "Pacific", "Southwest"])
        #
        #             ],
        #
        #             className="dropdown",
        #             # value='Pacific',
        #             # placeholder="View By Division",
        #             # multi=True
        #         )
        #     ],
        #
        #     className="dropdown-div"
        # ),

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
    Output("card-output", "children"),
    [Input("team-list", "value")]
)
def update_cards(division):
    if division is None:
        raise dash.exceptions.PreventUpdate

    if division == "All Teams":
        return [create_card(datum) for datum in json_data]

    # sort_cards: helper function from sort_cards_helper
    sorted_team_data = sort_cards(json_data, division)

    division_list = [ create_card(datum) for datum in sorted_team_data ]

    return division_list

if __name__ == '__main__':
    app.run_server(debug=True)