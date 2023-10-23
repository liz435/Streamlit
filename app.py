import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium
import json
import requests

st.title('New York Fire Department Calls')

# NYC
m = folium.Map(location=[40.7228, -73.9800], zoom_start=13)

#import local geojson file
geojson_data = json.load(open('PolicePrecincts.geojson'))

police_precincts_popups = []
for feature in geojson_data['features']:
    popup = feature['properties']['precinct']
    police_precincts_popups.append(folium.Popup(popup))

# Add the GeoJSON data to the map
folium.GeoJson(geojson_data, name='Police Precincts', popup=police_precincts_popups).add_to(m)

# Display the map
st.write('Police Precincts')
st_data = st_folium(m, height=725, width=725)


#add marker to the geojson
for feature in geojson_data['features']:
    popup = feature['properties']['precinct']
    folium.Marker(
        location=[feature['geometry']['coordinates'][1][0][0], feature['geometry']['coordinates'][0][0][0]],
        popup=popup,
        icon=folium.Icon(color='red', icon='fire-extinguisher', prefix='fa')
    ).add_to(m)

# Read the CSV data
df = pd.read_csv('https://data.cityofnewyork.us/resource/8m42-w767.csv')
df = df.dropna()

# Display the DataFrame
st.write(geojson_data['features'][0]['properties'])
st.title('New York Fire Department Calls')
st.write(df.head(10))

# Add CSS
st.markdown("""
<style>
body {
    color: black;
    background-color: #111;
}
</style>
    """, unsafe_allow_html=True)
