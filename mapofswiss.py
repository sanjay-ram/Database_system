import streamlit as st
import folium
from streamlit_folium import st_folium

# Wichtige Schweizer Städte + Koordinaten
locations = {
    "Aarau": [47.3916, 8.0514],
    "Basel": [47.5596, 7.5886],
    "Bern": [46.9480, 7.4474],
    "Biel/Bienne": [47.1367, 7.2468],
    "Chur": [46.8508, 9.5328],
    "Davos": [46.8022, 9.8355],
    "Fribourg": [46.8065, 7.1619],
    "Genf": [46.2044, 6.1432],
    "Glarus": [47.0404, 9.0670],
    "Lausanne": [46.5197, 6.6323],
    "Lugano": [46.0037, 8.9511],
    "Luzern": [47.0502, 8.3093],
    "Neuchâtel": [46.9911, 6.9319],
    "Schaffhausen": [47.6973, 8.6349],
    "Sitten (Sion)": [46.2330, 7.3606],
    "Solothurn": [47.2079, 7.5371],
    "St. Gallen": [47.4245, 9.3767],
    "Thun": [46.7587, 7.6269],
    "Winterthur": [47.4988, 8.7241],
    "Zug": [47.1662, 8.5155],
    "Zürich": [47.3769, 8.5417],
    "Bellinzona": [46.1954, 9.0293],
    "Locarno": [46.1690, 8.7910],
    "Schwyz": [47.0207, 8.6547],
    "Altdorf": [46.8802, 8.6443],
    "Herisau": [47.3866, 9.2792],
    "Appenzell": [47.3304, 9.4094],
    "Liestal": [47.4830, 7.7370],
    "Delémont": [47.3647, 7.3444],
    "Frauenfeld": [47.5573, 8.8988],
    "Sarnen": [46.8989, 8.2450],
    "Stans": [46.9583, 8.3661],
    "Glarus Nord": [47.1153, 9.0506],
    "Brig": [46.3180, 7.9878],
    "Martigny": [46.1028, 7.0741],
    "Leukerbad" :[46.3800, 7.6288]
}

st.title("🇨🇭 Interaktive Karte der Schweiz")

# Dropdown für Stadtwahl
city = st.selectbox("Wähle eine Stadt:", list(locations.keys()))

# Karte anzeigen
lat, lon = locations[city]
map = folium.Map(location=[lat, lon], zoom_start=11)
folium.Marker([lat, lon], popup=city).add_to(map)

st_folium(map, width=700, height=500)