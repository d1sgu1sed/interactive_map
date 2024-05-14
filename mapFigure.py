import pandas as pd
import geopandas as gpd
import plotly.graph_objects as go
import plotly.express as px
from shapely.geometry import Point
from random import * 


REGIONS = pd.read_parquet("data/russia_regions.parquet")
region_numbers = dict()


def convert_crs(x_arr, y_arr, to_crs='EPSG:32646', from_crs="EPSG:4326"):
    """Преобразование значений координат в массивах x_arr и y_arr
    из географической системы отсчёта from_crs в систему to_crs
    """
    data = [Point(x,y) for x,y in zip(x_arr, y_arr)]
    pts = gpd.GeoSeries(data, crs=from_crs).to_crs(to_crs)

    return pts.x, pts.y


class mapFigure(go.Figure):
    """ Шаблон фигуры для рисования поверх карты России
    """
    def __init__(self, 
        data=None, layout=None, frames=None, skip_invalid=False, # дефолтные параметры plotly
        **kwargs # аргументы (см. документацию к plotly.graph_objects.Figure())
    ):
        # создаём plotlу фигуру с дефолтными параметрами
        super().__init__(data, layout, frames, skip_invalid, **kwargs)

        # прорисовка регионов
        for i, r in REGIONS.iterrows():
            self.add_trace(go.Scatter(x=r.x, y=r.y,
                                      name=r.region,
                                      text=r.region,
                                      hoverinfo="text",
                                      line_color='grey',
                                      fill='toself',
                                      line_width=1,
                                      fillcolor='lightblue',
                                      showlegend=False,
            ))
            region_numbers[i] = r.region
            # print(region_numbers)
        
        # не отображать оси, уравнять масштаб по осям
        self.update_xaxes(visible=False)
        self.update_yaxes(visible=False, scaleanchor="x", scaleratio=1)

        # Если надо отображать города точками

        # df = pd.read_parquet("data/cities.parquet")
        # df['x'], df['y'] = convert_crs(df.lon, df.lat) 
        # self.add_trace(go.Scatter(
        #     x=df.x, y=df.y, name='города',
        #     text="<b>"+df.city+"</b>",
        #     hoverinfo="text", showlegend=False, mode='markers',
        #     marker_sizemode='area', marker_size=14,
        #     marker_color=px.colors.qualitative.G10
        # ))


        # чтобы покрасивее вписывалась карта на поверхности фигуры
        self.update_layout(showlegend=False, 
                           clickmode='event', dragmode='pan', 
                           width=1300, height=700, 
                           margin={'l': 50, 'b': 50, 't': 50, 'r': 50}) # отступы