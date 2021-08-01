import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table
from dash.dependencies import Input, Output

from helpers.draft_results_helper import get_lottery_picks
from app import app


layout = html.Div(
    [
        html.Hr(id="hr-draft"),

        html.H2(
            "NBA LOTTERY",
            style={
                "textAlign":"center",
                # "backgroundColor": "blue",
            }
        ),
        html.Div(
            html.A(
            dbc.Button(
                'HOME',
                className="home-button",
                style={'height': '3em', 'width': '8em', 'background-color': 'red', 'color': 'white'}
            ),
            href='/apps/start',
            style={"margin": "auto", "textAlign":"center", "align-items": "baseline",
                   "textDecoration":"none", "display":"center"}
            ),
            style={"justifyContent":"center", "display":"flex"}
        ),

        html.Hr(id="hr-draft"),

        # html.Div(
        #     id="first-round-draft-results"
        #
        # ),

        dbc.Tabs(
            [
                dbc.Tab(
                        label="First Round Pick",
                        id="first-round-pick",
                        active_label_style={"color":"white", "backgroundColor":"red"},
                        tab_style={'textAlign': 'center', 'backgroundColor':'blue'},
                ),

                dbc.Tab(
                        label="Second Round Pick",
                        id="second-round-pick",
                        active_label_style={"color":"white", "backgroundColor":"red"},
                        tab_style={'textAlign': 'center', 'backgroundColor':'blue'},
                )
            ],
            style={'justifyContent': 'center'}
        ),

        dcc.Interval(
           id='my_interval',
           interval=60000,
        )
    ],

    style={'width': '100%', "height":"100%","backgroundColor": "blue"}
)


@app.callback([Output('first-round-pick', 'children'),
               Output('second-round-pick', 'children')],
              [Input('my_interval', 'n_intervals')])
def fetch_draft(*args):
    df1, df2 = get_lottery_picks()

    table_1 = dash_table.DataTable(
        id='table',
        style_cell={'backgroundColor': 'blue'},
        style_header={'textAlign': 'center'},
        style_data={'textAlign': 'center'},
        fixed_columns={'headers': True, 'data': 1},
        fixed_rows={'headers': True},
        style_table={'minWidth': '100%'},
        columns=[{"name": i, "id": i} for i in df1.columns],
        data=df1.to_dict('records')
    )

    table_2 = dash_table.DataTable(
        id='table',
        style_cell={'backgroundColor': 'blue'},
        style_header={'textAlign': 'center'},
        style_data={'textAlign': 'center'},
        fixed_columns={'headers': True, 'data': 1},
        fixed_rows={'headers': True},
        style_table={'minWidth': '100%'},
        columns=[{"name": i, "id": i} for i in df2.columns],
        data=df2.to_dict('records')
    )

    return table_1, table_2



