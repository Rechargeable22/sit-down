import requests
import json
from typing import Any, Dict
import src.config as config

def download_bench_data() -> None:
    """
    Downloads bench data from OpenStreetMap using the Overpass API and prints the result.
    The data includes benches within a 1000 meter radius around Hamburg (53.555, 10.055).
    """
    # Coordinates for Hamburg
    lat, lon = 53.555, 10.055
    radius = 1000  # Search within 1000 meters

    # URL for the Overpass API
    overpass_url = "http://overpass-api.de/api/interpreter"
    # Overpass QL query for benches
    overpass_query = f"""
    [out:json];
    (
        node["amenity"="bench"](around:{radius},{lat},{lon});
    );
    out;
    """

    try:
        # Sending the GET request to the Overpass API
        response = requests.get(overpass_url, params={'data': overpass_query})
        # Ensuring the response status is successful
        response.raise_for_status()
        # Parsing the JSON response
        benches: Dict[str, Any] = response.json()
        with open(config.BENCHES_DATA_PATH, "w", encoding="utf-8") as file:
            json.dump(benches, file, ensure_ascii=False, indent=4)
            print(f"Data successfully saved to {config.BENCHES_DATA_PATH}")

    except requests.RequestException as e:
        # Handling request errors (e.g., network issues, invalid response)
        print(f"Failed to download data: {e}")

def main() -> None:
    """
    Main function to trigger the download of bench data.
    """
    download_bench_data()

if __name__ == "__main__":
    main()
