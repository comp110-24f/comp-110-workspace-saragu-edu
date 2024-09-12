def get_weather_report() -> str:
    weather: str = input("What is the weather?")
    if weather == "cold" or weather == "rainy":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there")
    else:
        print("I don't recognize this weather")
    return weather


age = age + 1
