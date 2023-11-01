import os
import sys

import requests


# Очистка экрана
def clear():
    command = "clear"

    # Смена команды очистки, если запущено на Windows
    if os.name in ("nt", "dow"):
        command = "cls"
    os.system(command)

# Приветственное сообщение и начало работы


def menu():
    print("Welcome to the Weather Application!")
    print("press s to start the application")
    print("press q to quit!")
    answer = input("")
    while (answer.lower() != "s" and answer.lower() != "q"):
        print("Please write s or q")
    return answer.lower()

# Получение необходимого города и единиц измерения


def weatherMenu():
    city = input("Write the name of the City you looking for: ")
    while len(city) == 0:
        city = input("Write the name of the City you looking for: ")
    units = input(
        "Write F to choose Fahrenheit or C to choose Celsius or K to choose Kelvin: ")
    while (len(units) == 0 or (units.lower() != "f" and units.lower() != "c" and units.lower() != "k")):
        units = input(
            "You entered wrong letter. Write F to choose Fahrenheit or C to choose Celsius or K to choose Kelvin: ")
    return {"city": city.capitalize(), "units": units.upper()}

# Получение погоды от API


def getWeather(city, units, API):
    link = f"http://localhost:5000/get-weather/{units}/{city}"
    r = requests.get(link)
    
    if r.status_code != 200:
        res = r.json()
        raise Exception(res['detail'])
    # Парсинг ответа от API
    try:
        data = r.json()
        weatherInfo = {
            "name": data["name"],
            "country": data["country"],
            "region": data["region"],
            "temperature": data["temperature"],
            "condition": data["condition"]
        }
        printInfo(weatherInfo, units.upper())
    except:
        print("You entered wrong city: ", city)
        sys.exit(0)

# Вывод погоды в удобном для понимании виде


def printInfo(info, units):
    text = f"""
        {info["name"]} - {info["region"]} - {info["country"]}
        Temperature: {info["temperature"]} {units}°
        Condition: {info["condition"]}
    """
    print(text)
