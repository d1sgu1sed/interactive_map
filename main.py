from dash import dash, dcc, html, Input, Output, callback, State
from pages import map_page, recipe_page, error_page
        
app = dash.Dash(__name__)

# Создаем макет страницы
app.layout = html.Div([
    dcc.Store(id='dummy', data='trigger-callback-on-page-load'),
    dcc.Store(id='saved_data'),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@callback(
    Output('page-content', 'children'),
    Input('url', 'pathname'),
    State('saved_data', 'data')
)
def display_page(pathname, saved_data):
    if pathname == '/recipe_page' and saved_data:
        return recipe_page.layout 
    elif pathname == '/':
        return map_page.layout
    else:
        return error_page.layout

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8050)