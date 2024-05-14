import dash
from dash import dcc
from dash import html, ctx
from mapFigure import mapFigure, region_numbers
from dash.dependencies import Input, Output
import plotly.graph_objects as go

        
app = dash.Dash(__name__)

fig = mapFigure()


# Создаем макет страницы
app.layout = html.Div([
    dcc.Graph(id="inter_map_graph", figure=fig),
    html.Span(id='prev_region', style={"font-size":"0px"}),
    html.Div(id='analytics_output'),
])


@app.callback(
    Output('analytics_output', 'children'),
    Output('inter_map_graph', 'figure'),
    Output('prev_region', 'children'),
    Input('inter_map_graph', 'clickData'),
    Input('prev_region', 'children')
    )
def update_y_timeseries(click_data, prev_region):
    num = click_data['points'][0]['curveNumber']
    
    fig['data'][num]['fillcolor']="#00ff00"
    print(prev_region)
    if prev_region or prev_region == 0:
        fig['data'][prev_region]['fillcolor']="lightblue"
    prev_region = num

    return f"Это - {region_numbers[num]}", fig, prev_region



if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8050)