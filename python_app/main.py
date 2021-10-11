import os
import sys
from os.path import join, dirname
from dotenv import load_dotenv
from functions import menu, clear, weatherMenu, getFahrenheit, getCelcius
open = True

dotenv_path = join(dirname(__file__), "..", '.env')
load_dotenv(dotenv_path)

API = os.environ.get("API")

while open:
    answer = menu()
    clear()
    if answer == "q":
        open = False
        clear()
    elif answer == "s":
        data = weatherMenu()
        city = data["city"]
        units = data["units"]
        print(f"City: {city}")
        print(f"Units: {units}")
        choice = input("Are you sure? (y/n): ")
        while choice.lower() != "y":
            clear()
            data = weatherMenu()
            city = data["city"]
            units = data["units"]
            print(f"City: {city}")
            print(f"Units: {units}")
            choice = input("Are you sure? (y/n): ")
        if choice.lower() == "y":
            if data["units"].lower() == "f":
                getFahrenheit(city, API)
            else:
                getCelcius(city, API)
        open = False
