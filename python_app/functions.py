import os
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
    while(answer.lower() != "s" and answer.lower() != "q"):
        print("Please write s or q")
    return answer.lower()

# Получение необходимого города и единиц измерения
def weatherMenu():
    city = input("Write the name of the City you looking for: ")
    while len(city) <= 0:
        city = input("Write the name of the City you looking for: ")
    units = input("Write F to choose Fahrenheit or C to choose Celsius: ")
    while(len(units) <= 0 or (units.lower() != "f" and units.lower() != "c")):
        units = input("Write F to choose Fahrenheit or C to choose Celsius: ")
    return {"city": city.capitalize(), "units": units.upper()}

# Получение погоды в Фаренгейтах от API
def getFahrenheit(city, API):
    link = "http://api.weatherstack.com/current"
    params = {'access_key': API, 'units': 'f', 'query': city}
    r = requests.get(link, params=params)
    
    # Парсинг ответа от API
    data = r.json()
    weatherInfo = {
        "name": data["location"]["name"],
        "country": data["location"]["country"],
        "region": data["location"]["region"],
        "time": data["current"]["observation_time"],
        "temperature": data["current"]["temperature"],
        "condition": data["current"]["weather_descriptions"][0]
    }
    printInfo(weatherInfo, "F")

# Получение погоды в Цельсиях от API
def getCelcius(city, API):
    link = "http://api.weatherstack.com/current"
    params = {'access_key': API, 'query': city}
    r = requests.get(link, params=params)
    
    # Парсинг ответа от API
    data = r.json()
    weatherInfo = {
        "name": data["location"]["name"],
        "country": data["location"]["country"],
        "region": data["location"]["region"],
        "temperature": data["current"]["temperature"],
        "condition": data["current"]["weather_descriptions"][0]
    }
    printInfo(weatherInfo, "C")

# Вывод погоды в удобном для понимании виде
def printInfo(info, units):
    text = f"""
        {info["name"]} - {info["region"]} - {info["country"]}
        Temperature: {info["temperature"]} {units}°
        Condition: {info["condition"]}
    """
    print(text)
