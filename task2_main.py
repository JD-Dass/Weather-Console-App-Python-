import requests
from task3_weather_api import fetch_weather, parse_weather
from task4_utils import get_cities, get_unit, display_weather

cities = get_cities()
unit = get_unit()

for city in cities:
    try:
        data = fetch_weather(city)
        weather = parse_weather(data)
        display_weather(weather, unit)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"city not found: {city}")
        else:
            print("Weather service error. Try later.")
    
    except requests.exceptions.ConnectionError:
        print("No internet connection, please check your network.")

    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    
    except Exception as e:
        print("Somthing went wrong. Try again later.")
        
