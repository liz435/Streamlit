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
fire = fire.to_dict()

most_fire_keys = list(fire.keys())
most_fire_string = str(most_fire_keys)

tier1 = str(most_fire_keys[0:9])
tier2 = str(most_fire_keys[10:19])
tier3 = str(most_fire_keys[20:29])
tier4 = str(most_fire_keys[30:39])
tier5 = str(most_fire_keys[40:49])
tier6 = str(most_fire_keys[50:59])
tier7 = str(most_fire_keys[60:69])
tier8 = str(most_fire_keys[70:])

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
        return '#7d0800'
    if feature['properties']['precinct'] in tier2:
        return '#8f1c14'
    if feature['properties']['precinct'] in tier3:
        return '#a63229'
    if feature['properties']['precinct'] in tier4:
        return '#ad4b44'
    elif feature['properties']['precinct'] in tier5:
        return '#bf6660'
    elif feature['properties']['precinct'] in tier6:
        return '#cf817c'
    elif feature['properties']['precinct'] in tier7:
        return '#de9c97'
    elif feature['properties']['precinct'] in tier8:
        return '#e6b9b5'
    else:
        return '#ebd7d5'
    
# Add the GeoJSON data to the map
folium.GeoJson(geojson_data, name='Police Precincts',
               tooltip=folium.GeoJsonTooltip(fields=('precinct', 'shape_area', 'shape_leng')),
               style_function= lambda feature: {'fillColor':field_type_colour(feature), 
                                                'fillOpacity':0.7, 'weight':1, 'color':'black', 'dashArray':'5, 5'}
                                                ).add_to(m)


# Display
st.write('Reported Fire Frequency by Police Precinct')
st.markdown("""
<div>
<button style = 'background-color:#7d0800;
                 text-decoration: none;
                 display:inline-block; 
                 border:none;
                 width:20px;
                 height:20px;
                '>
</button>
            <button style = 'background-color:#8f1c14;
                 text-decoration: none;
                 display:inline-block; 
                 border:none;
                 width:20px;
                 height:20px;
                '>
</button>

</button>
            <button style = 'background-color:#a63229;
                 text-decoration: none;
                 display:inline-block; 
                 border:none;
                 width:20px;
                 height:20px;
                '>
</button>
            
</button>
            <button style = 'background-color:#ad4b44;
                 text-decoration: none;
                 display:inline-block; 
                 border:none;
                 width:20px;
                 height:20px;
                '>
</button>
        
</button>
            <button style = 'background-color:#bf6660;
                 text-decoration: none;
                 display:inline-block; 
                 border:none;
                 width:20px;
                 height:20px;
                '>
</button>
            
</button>
            <button style = 'background-color:#cf817c;
                 text-decoration: none;
                 display:inline-block; 
                 border:none;
                 width:20px;
                 height:20px;
                '>
</button>
            
</button>
            <button style = 'background-color:#de9c97;
                 text-decoration: none;
                 display:inline-block; 
                 border:none;
                 width:20px;
                 height:20px;
                '>
</button>
            
</button>
            <button style = 'background-color:#e6b9b5;
                 text-decoration: none;
                 display:inline-block; 
                 border:none;
                 width:20px;
                 height:20px;
                '>
</button>
            
</button>
            <button style = 'background-color:#ebd7d5;
                 text-decoration: none;
                 display:inline-block; 
                 border:none;
                 width:20px;
                 height:20px;
                '>
</button>
</div>
            
            
    """, unsafe_allow_html=True)

st_data = st_folium(m, width=1280)
