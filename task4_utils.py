def get_cities():
    while True:
        try:
            count = int(input("How many cities do you want to check? (1-5): "))
            if 1 <= count <= 5:
                break
            else:
                print("Pleas enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")
    
    cities = []
    for i in range(count):
        city = input(f"Enter city {i + 1} name: ").strip()
        if city:
            cities.append(city)
        else:
            print("City name cannot be empty.")
    return cities

def display_weather(weather):
    print(f"===========================================")
    print(f"Weather Report")
    print(f"===========================================")
    print(f"city         : {weather['city']}")
    print(f"Temperature  : {weather['temperature']} °C")
    print(f"Humidity     : {weather['humidity']} %")
    print(f"Condition    : {weather['condition']}")
    print(f"===========================================")
        
        
        
        
        
        
        
        
    