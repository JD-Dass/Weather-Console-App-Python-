from task3_weather_api import fetch_weather, parse_weather
from task4_utils import get_cities, display_weather

cities = get_cities()

for city in cities:
    try:
        data = fetch_weather(city)
        weather = parse_weather(data)
        display_weather(weather)
    except Exception as e:
        print(f"Could not fetch weather for {city}")
