import os
from datetime import datetime
from dotenv import load_dotenv
import requests

load_dotenv()
load_dotenv()
API_KEY = os.getenv('API_KEY')


BASE_WEATHER_URL = "http://api.openweathermap.org/data/2.5"
BASE_LOC_URL =  "http://api.openweathermap.org/geo/1.0"


def suntimes_fetch(lat,lon):
    """gets data of the city the user put in based on coordinates from sunfetch function"""
    response_sun = requests.get(
        f"{BASE_WEATHER_URL}/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    )

    sun_status = response_sun.status_code
    if sun_status == 200:
        sun_data = response_sun.json()
        return sun_data
    else:
        return None, None
def sundata_processing(sun_data):
    """processes the data from suntimes_fetch function and prints these in a readable format"""
    sunrise_time = datetime.fromtimestamp(sun_data["sys"]["sunrise"])
    sunset_time = datetime.fromtimestamp(sun_data["sys"]["sunset"])
    print(f"Sunrise time: {sunrise_time.strftime("%H:%M:%S")}")
    print(f"Sunset time: {sunset_time.strftime("%H:%M:%S")}")