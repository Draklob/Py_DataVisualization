from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import json

# Explore the structure of the data.
# filename = 'data\eq_data_1_day_m1.json'
filename = 'data\eq_data_30_day_m1.json'
mags, lons, lats, hover_texts = [], [], [], []

def reading_data():
    with open(filename) as f:
        all_eq_data = json.load(f)

    all_eq_dicts = all_eq_data['features']
    for eq_dict in all_eq_dicts:
        mags.append(eq_dict['properties']['mag'])
        # mag = eq_dict['properties']['mag']
        lons.append(eq_dict['geometry']['coordinates'][0])
        lats.append(eq_dict['geometry']['coordinates'][1])
        hover_texts.append(eq_dict['properties']['title'])

def drawing_data():
    # Map the eartquakes.
    data = [{   # We create a dict key-value to be more structured.
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'marker': {
            'size': [5*mag for mag in mags],    # Using a list comprehension
            'color': mags,
            'colorscale': 'Viridis',    # dark blue to bright yellow
            'reversescale': True,     # we want bright yellow for lowest values and blue most severe.
            'colorbar': {'title': 'Magnitude'},
        },
    }]
    my_layout = Layout(title='Global Earthquakes')

    fig = {'data': data, 'layout': my_layout}
    offline.plot( fig, filename='global_earthquakes.html')

def run_script():
    reading_data()
    drawing_data()

# Uncomment the code below to run the script
#run_script()