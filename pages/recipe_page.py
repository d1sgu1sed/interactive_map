from dash import dcc, html, Input, Output, callback, State
import json


recipes = json.load(open('./data/recipes.json'))


layout = html.Div([
    html.H3(id='title'),
    html.Span(id='recipe'),
    html.Span(id='ingredients'),
    dcc.Link(id='go_back', href="/", className='go_back_btn')
])


@callback(
    Output('go_back', 'children'),
    Input('dummy', 'data')
    )
def delete_children(dummy):
    return '<- go back'

@callback(
    Output('title', 'children'),
    Output('recipe', 'children'),
    Output('ingredients', 'children'),
    Input(component_id='dummy', component_property='data'),
    # Input('url', 'search'))
    State('saved_data', 'data')
)
def display_value(dummy, saved_data):
    return recipes[str(saved_data)]['name'], recipes[str(saved_data)]['recipe'], json.dumps(recipes[str(saved_data)]['ingredients'])