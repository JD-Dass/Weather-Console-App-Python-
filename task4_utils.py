def get_city():
    while True:
        city = input("Enter city name: ").strip()
        if city:
            return city
        else:
            print("city name cannot be empty. Please try again.")

def display_weather(weather):
    print(f"===========================================")
    print(f"Weather Report")
    print(f"===========================================")
    print(f"city         : {weather['city']}")
    print(f"Temperature  : {weather['temperature']} °C")
    print(f"Humidity     : {weather['humidity']} %")
    print(f"Condition    : {weather['condition']}")
    print(f"===========================================")
        
        
        
        
        
        
        
        
    