import dash
import dash_bootstrap_components as dbc
import os

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY],
                meta_tags=[
                    {
                        'name':'viewport',
                        'content':'width=device-width, initial-scale=1.0, maximum-scale-1.2, minimum-scale=0.5'
                    }
                ],
                suppress_callback_exceptions=True)
server = app.server
server.secret_key = os.environ.get('secret_key', 'secret')
