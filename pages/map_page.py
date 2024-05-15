from dash import dcc, html, callback
from mapFigure import mapFigure, region_numbers, region_allowed_names, COLORS
from dash.dependencies import Input, Output, State

fig = mapFigure()

layout = html.Div([
        html.Div([
            html.Div([
                dcc.Graph(id="inter_map_graph", figure=fig, className='map-borders'),
            ]),
            html.Img(src='https://i.ibb.co/m0b1fmL/IMG-0116.png',
                    className='grand_img')
        ], className='upper-part'),
        html.Div([dcc.Link([], id='check_recipe', href="/recipe_page", className='check-recipe')], id='story_output', className='story-output'),
        # html.Div(id='prev_region', style={"font-size":"0px"}),
    ])


@callback(
    Output('story_output', 'children'),
    Output('inter_map_graph', 'figure'),
    Output('saved_data', 'data'),
    Input('dummy', 'data'),
    Input('inter_map_graph', 'clickData'),
    State('saved_data', 'data')
    )
def update_selected_region(dummy, click_data, saved_data):
    if click_data is None:
        if not(saved_data): 
            return '', fig, saved_data
        else:
            fig['data'][saved_data]['fillcolor'] = COLORS['usable']
            return f'{saved_data}', fig, saved_data
    
    num = click_data['points'][0]['curveNumber']
    region_name = region_numbers[num]

    if region_name not in region_allowed_names or num == saved_data:
        exit()
    
    fig['data'][num]['fillcolor'] = COLORS['selected']

    if saved_data or saved_data == 0:
        fig['data'][saved_data]['fillcolor'] = COLORS['usable']
    saved_data = num

    return [dcc.Link([], id='check_recipe', href="/recipe_page", className='check-recipe')], fig, saved_data
