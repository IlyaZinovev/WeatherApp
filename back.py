from requests import get
from os import getenv
from datetime import datetime, timedelta
import numpy as np
from json import loads

def get_today_date():
    return str(datetime.now()).split()[0]

def get_prev_date(days):
    return str(datetime.now() - timedelta(days=days-1)).split()[0]

def get_struct_data(city, days):
    result = dict()
    result['city'] = city
    result['from'] = get_prev_date(days)
    result['to'] = get_today_date()
    result['temperature_c'] = dict()
    result['humidity'] = dict()
    result['pressure_mb'] = dict()
    api_key = getenv("Weather_API_Key")
    temp_c = np.array([0] * 24)
    humidity = np.array([0] * 24)
    pressure_mb = np.array([0] * 24)
    while days > 1:
        date = get_prev_date(days)
        url = "https://api.weatherapi.com/v1/history.json?key={}&q={}&dt={}".format(api_key, city, date)
        response = loads(get(url).text)
        for hour in range(24):
            temp_c[hour] = response['forecast']['forecastday'][0]['hour'][hour]['temp_c']
            humidity[hour] = response['forecast']['forecastday'][0]['hour'][hour]['humidity']
            pressure_mb[hour] = response['forecast']['forecastday'][0]['hour'][hour]['pressure_mb']
        days -= 1
    result['temperature_c']['average'] = np.mean(temp_c)
    result['temperature_c']['median'] = np.median(temp_c)
    result['temperature_c']['min'] = np.min(temp_c)
    result['temperature_c']['max'] = np.max(temp_c)
    result['humidity']['average'] = np.mean(humidity)
    result['humidity']['median'] = np.median(humidity)
    result['humidity']['min'] = np.min(humidity)
    result['humidity']['max'] = np.max(humidity)
    result['pressure_mb']['average'] = np.mean(pressure_mb)
    result['pressure_mb']['median'] = np.median(pressure_mb)
    result['pressure_mb']['min'] = np.min(pressure_mb)
    result['pressure_mb']['max'] = np.max(pressure_mb)
    return result
