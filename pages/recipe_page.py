from dash import dcc, html, Input, Output, callback, State
import json


recipes = json.load(open('./data/recipes.json'))


layout = html.Div([
    # html.Script(),
    html.Div(className='main-container', children=[
        html.Div(id='name', className='name'),
        html.Div(className='mini-container', children=[
            html.Div(id='ingredients', className='ingredients'),
            html.Div([
                html.Div(id='photo', className='photo')
            ], className='photo-container')
        ]),
        html.Div(id='recipe', className='recipe')
    ]),
    html.A("Shopping list", id="openModal", className='shopping-list'),
    html.Div(id="myModal", className="modal", children=[
        html.Div(className="modal-content", children=[
            html.Span("×", id='close', className="close"),
            html.H2("Need to buy:"),
            html.Form( id='ingredients_window')
        ])
    ]),    
dcc.Link(id='go_back', href="/", className='go_back_btn')
], className='container-for-all')



@callback(
    Output('go_back', 'children'), 
    Output('name', 'children'),
    Output('recipe', 'children'),
    Output('ingredients', 'children'),
    Output('ingredients_window', 'children'),
    Output('photo', 'style'),
    Input('dummy', 'data'),
    State('saved_data', 'data')
)
def display_value(dummy, saved_data):
    ingrs = [html.Label(children=[key + ': ' + value if value else key
                ]) for key, value in recipes[str(saved_data)]['ingredients'].items()]
    inputs = [html.Label(children=[
                    dcc.Input(type="checkbox", name="product"), key + ': ' + value if value else key
                ]) for key, value in recipes[str(saved_data)]['ingredients'].items()]
    return ('<- go back', 
            recipes[str(saved_data)]['name'], 
            recipes[str(saved_data)]['recipe'], 
            ingrs,
            inputs,
            {'background-image': f"url('./assets/{saved_data}.png')"})


@callback(
    Output("myModal", "style", allow_duplicate=True),
    Input('openModal', 'n_clicks'),
    prevent_initial_call=True
)
def show_shopping_list(openModal):
    if openModal:
        return {'display': 'block'}


@callback(
    Output("myModal", "style"),
    Input('close', 'n_clicks')
)
def show_shopping_list(openModal):
    if openModal:
        return {'display': 'none'}