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

def get_unit():
    while True:
        unit = input("Choose temperature unit (C/F): ").strip().upper()
        if unit in ["C","F"]:
            return unit
        else:
            print("Please enter C or F only.")

def convert_temperature(temp_c, unit):
    if unit == "F":
        return (temp_c * 9/5) + 32
    return temp_c

def display_weather(weather, unit):
    temp = convert_temperature(weather["temperature"], unit)
    symbol = "°F" if unit == "F" else "°C"

    print(f"===========================================")
    print(f"Weather Report")
    print(f"===========================================")
    print(f"city         : {weather['city']}")
    print(f"Temperature  : {round(temp, 2)} {symbol}")
    print(f"Humidity     : {weather['humidity']} %")
    print(f"Condition    : {weather['condition']}")
    print(f"===========================================")
        
        
        
        
        
        
        
        
    