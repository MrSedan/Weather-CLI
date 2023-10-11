# Импортирование используемых библиотек
import os, sys
from os.path import join, dirname
from dotenv import load_dotenv

# Имортирование функций из другого файла
from functions import menu, clear, weatherMenu, getWeather
open = True

# Загрузка API-ключа из файла .env, либо его получение из системного окружения
dotenv_path = join(dirname(__file__), "..", '.env')
load_dotenv(dotenv_path)
API = os.environ.get("API")
if not API: 
    print("No API in environment or .env file given")
    sys.exit(0)

# Работа программы до тех пор пока пользователь не выберет что-либо
while open:
    answer = menu() # Выбор работы/выхода из программы
    clear() # Очистка консоли
    
    # Выбор работы программы в зависимости от ввода
    if answer == "q": # Выход из программы
        open = False
        clear()
    elif answer == "s": # Запуск программы
        choice = ''
        while choice.lower() != "y":
            clear()
            data = weatherMenu() # Спросить город и единицы измерения
            city = data["city"]
            units = data["units"]
            print(f"City: {city}")
            print(f"Units: {units}")
            choice = input("Are you sure? (y/n): ") # Спросить уверен ли пользователь в выборе
            
        # Получение погоды
        clear()
        getWeather(city, units, API)
        open = False
