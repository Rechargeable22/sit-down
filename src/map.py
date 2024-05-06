import folium
import json
import src.config as config

def create_map():
    # Load benches data from JSON file
    with open(config.BENCHES_DATA_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Create a map centered around the average location of all benches
    map = folium.Map(location=[53.555, 10.055], zoom_start=15)

    # Add markers for each bench
    for element in data['elements']:
        lat = element['lat']
        lon = element['lon']
        folium.Marker([lat, lon], tooltip='Bench').add_to(map)

    # Save the map as an HTML file
    map.save(config.SAMPLE_IMAGE_PATH)

    print("Map has been created and saved.")

if __name__ == "__main__":
    create_map()
