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

# team_df["first_name"] = player_metadata_df["first_name"]

ballislife_df = player_metadata_df.join(team_df)
print("SPAGHETTI: ", ballislife_df[["full_name", "name", "abbreviation"]])
print(ballislife_df.columns)

# main app layout
app.layout = dash_table.DataTable(ballislife_df,
                             id = 'table',
                             columns = [
                                 dict(
                                     name=col,
                                     id=col
                                 ) for col in ballislife_df.columns
                             ])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run_server(debug=True)