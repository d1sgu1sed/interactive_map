from pages import recipe_page
from dash import Input, Output, callback

@callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/recipe_page?key=word':
        return recipe_page 