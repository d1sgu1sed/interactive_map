from dash import dcc, html, Input, Output, callback, State
import json

layout = html.Div([
    html.Div(children='Incorrect page, go to the main page!', className='error-message'),   
    dcc.Link(id='go_back', href="/", className='go_back_btn', children='<- go back')
], className='container-for-all')
