import dash
import dash_core_components as dcc
import dash_html_components as html
<<<<<<< HEAD
=======
import pandas
import plotly.express as px
import pandas as pd
import requests
import dash
>>>>>>> player_refactor
import dash_bootstrap_components as dbc

from card.init_data import card_data
from card.create_container import create_card

# app start
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div(
            children=[
                html.Div(
                        [   # dropdown skeleton
                            dcc.Dropdown(
                                id='team-list',
                                options=[
                                    # {"label": i, "value": i}
                                    # for i in [card_data]
                                    {"label": "New York", "value": 'NYC'},
                                    {"label": "Los Angeles", "value": 'LA'},
                                    {"label": "Boston", "value": 'MA'}

                                ],

<<<<<<< HEAD
                                value=['LAL'],
                                placeholder="Select Sport",
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
                ],
=======
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
>>>>>>> player_refactor
            )

if __name__ == '__main__':
    app.run_server(debug=True)