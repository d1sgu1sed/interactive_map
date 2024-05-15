from dash import html, Input, Output, callback

layout = html.Div([
    html.H3('Page 1'),
    html.Span(id='span-view')
])


@callback(
    Output('span-view', 'children'),
    Input('page-1-dropdown', 'value'))
def display_value(value):
    return f'Your get requests {value}'