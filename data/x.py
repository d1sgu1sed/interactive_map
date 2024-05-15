from pyproj import Proj, transform
import pandas as pd
import json


names = ['Улан-Удэ', 'Санкт-Петербург', 'Петропавловск-Камчатский', 
         'Екатеринбург', 'Казань']
with open('/russian-cities.json') as f:
    file = json.load(f)

cities_data = {
    'city': [],
    "lon": [],
    "lat": [],
}

for city in file:
    if city['name'] in names:
        cities_data['city'].append(city['name'])
        cities_data['lon'].append(float(city['coords']['lon']))
        cities_data['lat'].append(float(city['coords']['lat']))

print(cities_data)

in_proj = Proj(init='epsg:4236')
out_proj = Proj(init='epsg:4236')

cities_data['lon'], cities_data['lat'] = transform(in_proj, out_proj, cities_data['lon'], cities_data['lat'])

cities_df = pd.DataFrame(cities_data)

cities_df.to_parquet('./data/cities.parquet')