import dash
import dash_auth
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import request
import pandas as pd

df = pd.read_csv('auth.csv')

VALID_USERNAME_PASSWORD_PAIRS = dict(df[['username', 'password']].values.tolist())

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.layout = html.Div([

    html.H2(id='show-output', children=''),
    html.Button('press to show username', id='button')

], className='container')

@app.callback(
    Output(component_id='show-output', component_property='children'),
    [Input(component_id='button', component_property='n_clicks')]
)
def update_output_div(n_clicks):
    username = request.authorization['username']
    if n_clicks:
        info = list(df['username' == username])
        return info
    else:
        return ''

app.scripts.config.serve_locally = True


if __name__ == '__main__':
    app.run_server(debug=True)