from geopy import Yandex
import json
def togeojson(region, city, street_name, street_number):
    country = "Россия"
    place = f"{city}, {street_name}, {street_number}"
    location = Yandex(api_key='3d073a9b-81f9-4e5b-b991-595f534a1eed').geocode(place)
    lat, lng = location.latitude, location.longitude
    geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "coordinates": [
                    lng,
                    lat
                    ],
                    "type": "Point"
                }
            }
        ]
    }
    return json.dumps(geojson, indent=2)
print(togeojson("Москвовская область", "Москва", "Заречная", 7))
