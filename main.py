import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from card.init_data import card_data
from card.create_container import create_card

# app start
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY],
                meta_tags=[{
                    'name':'viewport',
                    'content':'width=device-width, initial-scale=1.0, maximum-scale-1.2, minimum-scale=0.5'}])

app.layout = html.Div(
    children=[
        html.Div(
            [   # dropdown skeleton
                dcc.Dropdown(
                    id="team-list",
                    options=[
                        {"label": i, "value": i}
                        for i in sorted(["Atlantic", "Southeast", "Central", "Northwest", "Pacific", "Southwest"])

                    ],


                    className="dropdown",
                    value=['LAL'],
                    placeholder="View By Division",
                    multi=True
                )
            ],

            className="dropdown-div"
            # style={
            #     "width": "25%",
            #     "margin-left": "475px",
            #     "margin-top":"10px",
            #     "margin-bottom":"10px",
            #     "verticalAlign":"middle",
            #     "color":"#000000"
            # }
        ),

        html.Div(
            [
                create_card(datum)

                for datum in card_data
            ],

            id="card-output",
            className="card-grid"
        )
    ],

    className="outermost-div"
)


if __name__ == '__main__':
    app.run_server(debug=True)