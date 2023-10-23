import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import json

st.title('New York Fire Department Calls')

#Fire Data
df = pd.read_csv('https://data.cityofnewyork.us/resource/8m42-w767.csv')
df = df.dropna()
# Read the CSV data

fire = df['policeprecinct'].value_counts()
most_fire = dict(fire)
# Get the keys of the dictionary

most_fire_keys = sorted(most_fire, key=most_fire.get, reverse=True)

most_fire_string = str(most_fire_keys)

tier1 = most_fire_string[:9]
tier2 = most_fire_string[10:19]
tier3 = most_fire_string[20:29]
tier4 = most_fire_string[30:39]
tier5 = most_fire_string[40:49]
tier6 = most_fire_string[50:59]
tier7 = most_fire_string[60:69]
tier8 = most_fire_string[70:]

st.write(tier1)

# NYC
m = folium.Map(location=[40.7228, -73.8000], zoom_start=12, width=1280, height=720)

#import local geojson file
geojson_data = json.load(open('PolicePrecincts.geojson'))

police_precincts_popups = []
for feature in geojson_data['features']:
    popup = feature['properties']['precinct']
    police_precincts_popups.append(popup)

# st.write(police_precincts_popups)

def field_type_colour(feature):
    if feature['properties']['precinct'] in tier1:
        return 'darkred'
    if feature['properties']['precinct'] in tier2:
        return 'red'
    if feature['properties']['precinct'] in tier3:
        return 'orange'
    if feature['properties']['precinct'] in tier4:
        return 'yellow'
    elif feature['properties']['precinct'] in tier5:
        return 'green'
    elif feature['properties']['precinct'] in tier6:
        return 'grey'
    elif feature['properties']['precinct'] in tier7:
        return 'black'
    elif feature['properties']['precinct'] in tier8:
        return 'beige'
    
# Add the GeoJSON data to the map
folium.GeoJson(geojson_data, name='Police Precincts',
               tooltip=folium.GeoJsonTooltip(fields=('precinct', 'shape_area', 'shape_leng')),
               style_function= lambda feature: {'fillColor':field_type_colour(feature), 
                                                'fillOpacity':0.5, 'weight':1, 'color':'black', 'dashArray':'5, 5'}
                                                ).add_to(m)


# Display the map
st.write('Police Precincts')
st_data = st_folium(m, width=1280)


# Add CSS
st.markdown("""
<style>
body {
    color: black;
    background-color: #111;
}
</style>
    """, unsafe_allow_html=True)
