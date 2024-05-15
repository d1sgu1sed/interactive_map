from dash import dash, dcc, html, Input, Output, callback
from pages import map_page, recipe_page
        
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
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/recipe_page':
        return recipe_page.layout 
    elif pathname == '/':
        return map_page.layout
    else:
        return pathname

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8050)