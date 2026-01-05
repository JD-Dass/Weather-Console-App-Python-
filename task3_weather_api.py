import requests
from task1_config import API_KEY, BASE_URL

def  fetch_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

def parse_weather(data):
    weather_info = {
        "city": data.get("name", "N/A"),
        "temperature": data.get("main", {}).get("temp", "N/A"),
        "humidity": data.get("main", {}).get("humidity", "N/A"),
        "condition": data.get("weather", [{}])[0].get("description", "N/A")
    }
    return weather_info