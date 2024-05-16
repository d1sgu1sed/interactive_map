from dash import dcc, html, callback
from mapFigure import mapFigure, region_numbers, region_allowed_names, COLORS
from dash.dependencies import Input, Output, State
import json
import random

fig = mapFigure()

replics = json.load(open('./data/words.json'))

layout = html.Div([
        html.Div([
            html.Div([
                dcc.Graph(id="inter_map_graph", figure=fig),
            ]),
            html.Img(src='https://i.ibb.co/m0b1fmL/IMG-0116.png',
                    className='grand_img')
        ], className='upper-part'),
        html.Div(id='story_output', className='story-output'),
        dcc.Link(id='check_recipe', href="/recipe_page", className='recipe_btn', children="read the recipe ->", style={'visibility': 'hidden'})
        # html.Div(id='prev_region', style={"font-size":"0px"}),
    ])


@callback(
    Output('check_recipe', 'style'),
    Input('inter_map_graph', 'clickData'),
    Input('dummy', 'data')
    )
def show_btn(click_data, dummy):
    if click_data is None or str(click_data['points'][0]['curveNumber']) not in replics.keys():
        return {'visibility': 'hidden'}
    elif str(click_data['points'][0]['curveNumber']) in replics.keys():
        return {'visibility': 'visible'}


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
            # Покраска регионов из файла в синий
            for i in replics.keys():
                if i.isdigit():
                    fig['data'][int(i)]['fillcolor'] = COLORS['usable']
                else:
                    break
            return replics['hello'], fig, saved_data
        else:
            fig['data'][saved_data]['fillcolor'] = COLORS['usable']
            return replics['cook' + str(random.randint(1, 4))], fig, saved_data
    
    num = click_data['points'][0]['curveNumber']
    region_name = region_numbers[num]
    if region_name not in region_allowed_names:
        exit()
    fig['data'][num]['fillcolor'] = COLORS['selected']

    if num == saved_data:
        return replics[str(num)], fig, saved_data
    

    if saved_data or saved_data == 0:
        fig['data'][saved_data]['fillcolor'] = COLORS['usable']
    saved_data = num

    return replics[str(num)], fig, saved_data
