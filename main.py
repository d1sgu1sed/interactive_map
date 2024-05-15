import dash
from dash import dcc
from dash import html
from mapFigure import mapFigure, region_numbers, region_allowed_names, COLORS
from dash.dependencies import Input, Output
import plotly.graph_objects as go
# import callbacks
        
app = dash.Dash(__name__, suppress_callback_exceptions=True)

fig = mapFigure()


# Создаем макет страницы
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.Div([
            html.Div([
                dcc.Graph(id="inter_map_graph", figure=fig, className='map-borders'),
            ]),
            html.Img(src='https://i.ibb.co/m0b1fmL/IMG-0116.png',
                    className='grand_img')
        ], className='upper-part'),
        html.Div([dcc.Link(id='check_recipe', href="/recipe_page?key=word", title='lol' , className='check-recipe')], id='story_output', className='story-output'),
        html.Span(id='prev_region', style={"font-size":"0px"}),
    ], id='page-content')])


@app.callback(
    Output('story_output', 'children'),
    Output('inter_map_graph', 'figure'),
    Output('prev_region', 'children'),
    Input('inter_map_graph', 'clickData'),
    Input('prev_region', 'children')
    )
def update_selected_region(click_data, prev_region):
    num = click_data['points'][0]['curveNumber']
    region_name = region_numbers[num]

    if region_name not in region_allowed_names or num == prev_region:
        return f"Welcome, my Vnuchok. This is Buryatiya - {region_numbers[prev_region]}", fig, prev_region
    
    fig['data'][num]['fillcolor']=COLORS['selected']

    if prev_region or prev_region == 0:
        fig['data'][prev_region]['fillcolor']=COLORS['usable']
    prev_region = num

    return f"Welcome, my Vnuchok. This is Buryatiya - {region_name}", fig, prev_region





if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8050)