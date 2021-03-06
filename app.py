from flask import Flask, request
from requests import get
from os import getenv
from datetime import datetime, timedelta
import numpy as np
from json import loads, dumps

def get_today_date():
    return str(datetime.now()).split()[0]

def get_prev_date(days):
    return str(datetime.now() - timedelta(days=days-1)).split()[0]

def api_key():
    return getenv("Weather_API_Key")

def url_for_request(city, date):
    return "https://api.weatherapi.com/v1/history.json?key={}&q={}&dt={}".format(api_key(), city, date)

app = Flask(__name__)


@app.route("/weather")
def get_weather():
    city = request.args.get("city", "")
    days = int(request.args.get("days", ""))
    temp_c = np.zeros(24)
    humidity = np.zeros(24)
    pressure_mb = np.zeros(24)
    for day in range(1, days + 1):
        date = get_prev_date(day)
        response = loads(get(url_for_request(city, date)).text)
        for hour in range(24):
            temp_c[hour] = response['forecast']['forecastday'][0]['hour'][hour]['temp_c']
            humidity[hour] = response['forecast']['forecastday'][0]['hour'][hour]['humidity']
            pressure_mb[hour] = response['forecast']['forecastday'][0]['hour'][hour]['pressure_mb']
    result = {
        'city': city,
        'from': get_prev_date(days),
        'to': get_today_date(),
        'temperature_c': {
            'average': np.mean(temp_c),
            'median': np.median(temp_c),
            'min': np.min(temp_c),
            'max': np.max(temp_c)
            },
        'humidity': {
            'average': np.mean(humidity),
            'median': np.median(humidity),
            'min': np.min(humidity),
            'max': np.max(humidity)
            },
        'pressure_mb': {
            'average': np.mean(pressure_mb),
            'median': np.median(pressure_mb),
            'min': np.min(pressure_mb),
            'max': np.max(pressure_mb)
            }
        }    
    return dumps(result)
