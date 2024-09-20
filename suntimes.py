import os
from datetime import datetime
from dotenv import load_dotenv
from collections import defaultdict
import requests

load_dotenv()
load_dotenv()
API_KEY = os.getenv('API_KEY')


BASE_WEATHER_URL = "http://api.openweathermap.org/data/2.5"
BASE_LOC_URL =  "http://api.openweathermap.org/geo/1.0"

def sun_locationfetch(sun_city):
    """gets coordinates of the city the user put in"""
    response_loc = requests.get(f"{BASE_LOC_URL}/direct?q={sun_city}&limit=1&appid={API_KEY}")
    location_status = response_loc.status_code
    if location_status == 200:
        sun_location = response_loc.json()
        if sun_location:
            sun_lat = sun_location[0]["lat"]
            sun_lon = sun_location[0]["lon"]
            return sun_lat, sun_lon
    else:
        return None, None
def suntimes_fetch(sun_lat,sun_lon):
    """gets data of the city the user put in based on coordinates from sunfetch function"""
    response_sun = requests.get(
        f"{BASE_WEATHER_URL}/forecast?lat={sun_lat}&lon={sun_lon}&appid={API_KEY}&units=metric"
    )
    sun_status = response_sun.status_code
    if sun_status == 200:
        sun_data = response_sun.json()
        return sun_data
    else:
        return None, None
def sunprocessing(sun_data):
    """processes the data from suntimes_fetch function and prints these in a readable format"""
    sunrise_time = datetime.fromtimestamp(sun_data["city"]["sunrise"])
    sunset_time = datetime.fromtimestamp(sun_data["city"]["sunset"])
    print(f"Sunrise time: {sunrise_time}")
    print(f"Sunset time: {sunset_time}")