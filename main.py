import dash
from dash import dcc
from dash import html
from mapFigure import mapFigure
from dash.dependencies import Input, Output
import json

        
app = dash.Dash(__name__)

fig = mapFigure()


# Создаем макет страницы
app.layout = html.Div([
    dcc.Graph(id="inter_map_graph", figure=fig),
    html.Div(id='analytics_output', style={"height":"200px"})
])


@app.callback(
    Output('analytics_output', 'children'),
    Input('inter_map_graph', 'clickData'))
def update_y_timeseries(click_data):
    return json.dumps(click_data, indent=2)

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8050)