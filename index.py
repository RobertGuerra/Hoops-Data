import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import start, selected


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):

    if pathname == '/' or pathname =='/apps/start':
        return start.layout
    elif '/apps/selected' in pathname:
        return selected.layout
    else:
        return '404'


# '0.0.0.0', 5001
if __name__ == '__main__':
    app.run_server(debug=True)
