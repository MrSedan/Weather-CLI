import os
from os.path import dirname, join
from typing import Annotated

import aiohttp
import uvicorn
from dotenv import load_dotenv
from fastapi import Body, FastAPI, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from pydantic import BaseModel


class WeatherRequest(BaseModel):
    city: str | int

dotenv_path = join(dirname(__file__), "..", '.env')
load_dotenv(dotenv_path)
API_KEY = os.environ.get("API")


API_URL = "http://api.weatherstack.com/current"

description = """
Веб-сервер для скрипта получения температуры в городе
"""

app = FastAPI(description=description)


@app.post('/get-weather/{temp_type}')
async def get_weather(*, data: Annotated[WeatherRequest, Body(
    openapi_examples={
        "normal": {
            "summary": "A normal example",
            "description": "A **normal** item works correctly.",
            'value': {
                "city": "Kirov"
            }
        },
        "invalid": {
            "summary": "Invalid city",
            "description": "A **bad** throws 400 error",
            "value": {
                "city": 123,
            }
        },
    }
    )], temp_type: str = "c"):
    """
    Метод получения погоды по полученному городу и единице измерения
    """
    if type(data.city) != str:
        raise HTTPException(status_code=400, detail="Bad city")
    if temp_type not in ['k', 'f', 'c']:
        raise HTTPException(status_code=400, detail="Bad temperature type")
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL, params={'access_key': API_KEY, 'query': data.city}, headers={'Content-Type': 'application/json'}) as resp:
            if resp.status != 200:
                raise HTTPException(400, detail='Bad city')
            data = await resp.json()
            return {"temperature": data['current']['temperature']}


@app.get('/swagger')
async def swagger_page():
    """
    Метод получения страницы с документацией по методам
    """
    return get_swagger_ui_html(openapi_url='/openapi.json', title='Weather docs')

if __name__ == '__main__':
    uvicorn.run("main:app", port=5000, reload=True, log_level="info")