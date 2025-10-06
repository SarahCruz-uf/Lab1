#add libraries for making a request and using json data
import requests
import json
#potential libraries for open meteo requests
#import openmeteo_requests
#import requests_cache
#from retry_requests import retry

# function to request latitude and longitude for a city
def get_coordinates(city_name):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    
    response = requests.get(geo_url)
    response.raise_for_status()
    data = response.json()

    if "results" in data and data["results"]:  # checks if results exist
        result = data["results"][0]
        latitude = result["latitude"]
        longitude = result["longitude"]
        country = result.get("country", "Unknown")
        return {"city": city_name, "latitude": latitude, "longitude": longitude, "country": country}
    else:
        print(f"{city_name} is not found in the geocoding database.")
        return None

# function to save data to json then print it
def save_coordinates(data, city_name):
    filename = f"{city_name.replace(' ', '_')}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"{city_name} is located at: {data['latitude']}, {data['longitude']}")
    print(f"Country: {data['country']}")


if __name__ == "__main__":
    city_name = input("Enter a city name: ").strip()
    coordinates = get_coordinates(city_name)
    if coordinates:
        save_coordinates(coordinates, city_name)

