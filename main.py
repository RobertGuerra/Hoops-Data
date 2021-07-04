import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas
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

# combining player first and last name
player_metadata_df['Player'] = player_metadata_df['first_name'] + ' ' + player_metadata_df['last_name']
player_metadata_df['first_name'] = player_metadata_df['Player']

# dropping fields and renaming Player column
player_metadata_df.drop(["last_name", "Player"], axis=1, inplace=True)
player_metadata_df.rename(columns={'first_name':'Player'}, inplace=True)

# combining player Height
player_metadata_df['height_feet'] = player_metadata_df['height_feet'].astype(str)
player_metadata_df['height_inches'] = player_metadata_df['height_inches'].astype(str)
player_metadata_df['height_feet'] = player_metadata_df['height_feet'] + ' ' + player_metadata_df['height_inches']
player_metadata_df.drop('height_inches', axis=1, inplace=True)
player_metadata_df.rename(columns={'height_feet':'player_height'}, inplace=True)


# separated team metadata
team_df = pd.DataFrame.from_records(temp_df["team"])
team_df["team_id"] = team_df["id"]
team_df["abbr"] = team_df["abbreviation"]

# dropping some fields and renaming Team column
team_df = team_df.drop(["id","abbreviation", "city", "name"], axis=1)
team_df.rename(columns={'full_name':'Team Name'}, inplace=True)



# final dataframe
ballislife_df = player_metadata_df.join(team_df).drop(['player_id','team_id'], axis=1)


# main app layout
app.layout = html.Div(
            dash_table.DataTable(
                data=ballislife_df.to_dict('records'),
                id = 'table',
                style_cell=dict(
                    backgroundColor='black'
                ),
                columns = [
                        dict(
                            name=col,
                            id=col
                            ) for col in ballislife_df.columns
                        ])
            )

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run_server(debug=True)