import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import requests
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import json
import dash_table

response = requests.get('https://www.balldontlie.io/api/v1/players')
res_json = json.loads(response.content)
data = res_json["data"]

# Initialize Application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# json content into df
temp_df = pd.DataFrame.from_records(data)

# separated player metadata
player_metadata_df = temp_df.drop("team", axis=1) # axis=1 specifies column-wise drop
player_metadata_df["player_id"] = player_metadata_df["id"]
player_metadata_df = player_metadata_df.drop("id", axis=1)

# separated team metadata
team_df = pd.DataFrame.from_records(temp_df["team"])
team_df["team_id"] = team_df["id"]
team_df = team_df.drop("id", axis=1)

# creating final df
ballislife_df = player_metadata_df.join(team_df).drop(["player_id", "team_id", "city", "name"], axis=1).astype(str)
ballislife_df = ballislife_df.replace(['nan', ''], 'N/A')

# Polishing df, changing column style
ballislife_df.columns = [col.replace("_", " ").title() for col in ballislife_df.columns]


# main app layout
app.layout = html.Div(
    [
        html.H1(
            "Hoops Data",
            style=dict(
                textAlign="center"
            )
        ),

        dash_table.DataTable(
            data=ballislife_df.to_dict('records'),
            id = 'table',

            columns = [
                dict(
                    name=col,
                    id=col
                ) for col in ballislife_df.columns
            ],

            style_data=dict(
                textAlign="center",
                border='1px solid blue'
            ),

            style_header=dict(
                textAlign="center"
            ),

            style_data_conditional=[
                {
                    'if': {
                        'filter_query': '{{{}}} = "N/A"'.format(col),
                        'column_id': col
                    },
                    'color': 'red'

                } for col in ballislife_df.columns
            ],

            style_cell=dict(
                backgroundColor="black",
                fontFamily="Helvetica, serif"
            )
        )
    ]
)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run_server("0.0.0.0", 5000, debug=True)