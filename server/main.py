import os
from os.path import dirname, join
from typing import Annotated

import aiohttp
import uvicorn
from dotenv import load_dotenv
from fastapi import Body, Depends, FastAPI, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass


@dataclass
class QueryParams:
    city: str
    temp_type: str


dotenv_path = join(dirname(__file__), "..", '.env')
load_dotenv(dotenv_path)
API_KEY = os.environ.get("API")


API_URL = "http://api.weatherstack.com/current"

description = """
Веб-сервер для скрипта получения температуры в городе
"""

app = FastAPI(description=description)


@app.get('/get-weather/{temp_type}/{city}')
async def get_weather(data: QueryParams = Depends()):
    """
    Метод получения погоды по введенному городу и единице измерения
    """
    temp_type = data.temp_type.casefold()
    city = data.city.capitalize()
    if not len(city):
        raise HTTPException(status_code=400, detail="You entered wrong city")
    if temp_type not in ['k', 'f', 'c']:
        raise HTTPException(status_code=400, detail="You entered wrong temperature type")
    params = {'access_key': API_KEY, 'query': city}
    if temp_type == 'f':
        params['units'] = 'f'
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(API_URL, params=params) as resp:
                data = await resp.json()
                if resp.status != 200 or ('success' in data and not data['success']):
                    raise HTTPException(400, detail='You entered wrong city')
                return {
                    "temperature": data['current']['temperature'] + (273.15 if temp_type == 'k' else 0), 
                    "country": data['location']['country'], 
                    "name": data['location']['name'], 
                    "region": data['location']['region'], 
                    "condition": data["current"]["weather_descriptions"][0],
                    "time": data['current']['observation_time']
                    }
        except HTTPException as e:
            raise e
        except:
            raise HTTPException(500, detail="Weather server is unreachable")


@app.get('/swagger')
async def swagger_page():
    """
    Метод получения страницы с документацией по методам
    """
    return get_swagger_ui_html(openapi_url='/openapi.json', title='Weather docs')

if __name__ == '__main__':
    uvicorn.run("main:app", port=5000, reload=True, log_level="info")
