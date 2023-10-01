# Импортирование используемых библиотек
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Имортирование функций из другого файла
from functions import menu, clear, weatherMenu, getFahrenheit, getCelcius
open = True

# Загрузка API-ключа из файла .env, либо его получение из системного окружения
dotenv_path = join(dirname(__file__), "..", '.env')
load_dotenv(dotenv_path)
API = os.environ.get("API")

# Работа программы до тех пор пока пользователь не выберет что-либо
while open:
    answer = menu() # Выбор работы/выхода из программы
    clear() # Очистка консоли
    
    # Выбор работы программы в зависимости от ввода
    if answer == "q": # Выход из программы
        open = False
        clear()
    elif answer == "s": # Запуск программы
        data = weatherMenu() # Спросить город и единицы измерения
        city = data["city"]
        units = data["units"]
        print(f"City: {city}")
        print(f"Units: {units}")
        choice = input("Are you sure? (y/n): ") # Спросить уверен ли пользователь в выборе
        
        # Повторение вопроса, если человек ответил n
        while choice.lower() != "y":
            clear()
            data = weatherMenu()
            city = data["city"]
            units = data["units"]
            print(f"City: {city}")
            print(f"Units: {units}")
            choice = input("Are you sure? (y/n): ")
            
        # Получение погоды
        if choice.lower() == "y":
            clear()
            
            # Вывод погоды в зависимости от выбранных единиц
            if data["units"].lower() == "f":
                getFahrenheit(city, API)
            else:
                getCelcius(city, API)
        open = False
