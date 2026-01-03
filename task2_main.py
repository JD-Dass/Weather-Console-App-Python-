from task3_weather_api import fetch_weather, parse_weather
from task4_utils import get_city, display_weather

city = get_city()
data = fetch_weather(city)
weather = parse_weather(data)

display_weather(weather)
