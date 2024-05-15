from dash import dcc, html, Input, Output, callback, State

layout = html.Div([
    html.H3('Page 1'),
    html.Span(id='span-view'),
    dcc.Link(id='go_back', href="/", className='go_back_btn')
])

@callback(
    Output('go_back', 'children'),
    Input('dummy', 'data')
    )
def delete_children(dummy):
    return ''

@callback(
    Output('span-view', 'children'),
    Input(component_id='dummy', component_property='data'),
    # Input('url', 'search'))
    State('saved_data', 'data')
)
def display_value(dummy, saved_data):
    return f'Your get requests {saved_data}'