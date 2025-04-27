import folium
# data science from sanjay
swiss_map = folium.Map(location=[46.8182, 8.2275], zoom_start=8)

zurich_map = folium.Map(location=[47.3769, 8.5417], zoom_start=12)

bern_map = folium.Map(location=[46.9480, 7.4474], zoom_start=12)

bern_map.show_in_browser()