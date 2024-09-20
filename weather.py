import os

import requests
from collections import defaultdict
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


BASE_WEATHER_URL = "http://api.openweathermap.org/data/2.5"
BASE_LOC_URL =  "http://api.openweathermap.org/geo/1.0"


def usrinput():
        """gets inport from user on where to get the weather from and the amount of days"""
        city = input("Which place would you like to know the weather forecast of? ").strip()
        try:
            cnt = int(input("For many days would you like to know the weather forecast? (max. 5) ").strip())
            if cnt > 5:
                print("that is more than 5 days; you will now get the forecast for the coming 5 days.")
                cnt = 5
            return city, cnt
        except ValueError:
            print("Please enter a number.")
            return usrinput()

def locationfetch(city):
    """gets the coordinates of the city the user put in"""
    response_location = requests.get(f"{BASE_LOC_URL}/direct?q={city}&limit=1&appid={API_KEY}")
    loc_status = response_location.status_code
    return loc_status, response_location
def locationprocessing(status, response_location):
    """extracts the longitude and latitude of the location out of the API-response"""
    # Check if the request was successful
    if status == 200:
        locatie = response_location.json()

        if locatie:
            lat = locatie[0]["lat"]
            lon = locatie[0]["lon"]
            return lat, lon
    else:
        print(f"Error getting location data: {response_location.status_code}")
        return None, None

def weatherfetch(lat,lon):
        """gets the weather forecast based of the coordinates provided by the geo-API"""
        # Get weather data using latitude and longitude
        response_weather = requests.get(
        f"{BASE_WEATHER_URL}/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        )
        weather_status = response_weather.status_code
        return weather_status, response_weather

def weatherprocessing(weather_status, response_weather, cnt, city):
    """extracts the data needed from the weather-API's response and prints it in a readable format"""

    if weather_status == 200:
        weather_data = response_weather.json()


        # Grouping data by day
        daily_data = defaultdict(list)
        print("_"* 40)
        print(f"weather for coming {cnt} days in {city}")
        print("_" * 40)
        days_count = 0
        for forecast in weather_data['list']:
            # Get date and time from the forecast
            forecast_time = datetime.fromtimestamp(forecast['dt'])
            date_str = forecast_time.date()

            # Collect the temperature and weather description
            temp = forecast['main']['temp']
            weather_desc = forecast['weather'][0]['description']

            daily_data[date_str].append({
                'time': forecast_time,
                'temp': temp,
                'description': weather_desc
            })


        #getting data into a readable format and printing it
        for day, forecasts in daily_data.items():
                # Calculate average temperature for the day
            avg_temp = sum([f['temp'] for f in forecasts]) / len(forecasts)

            # Get the most common weather description for the day
            most_appearing_weather = max(set([f['description'] for f in forecasts]), key=[f['description'] for f in forecasts].count)

            # shows grouped daily forecast in a readable format
            print(f"Date: {day.strftime('%d/%m/%Y')}")
            print(f"Average Temp: {avg_temp:.1f}°C")
            print(f"Weather: {most_appearing_weather}")
            print('_' * 40)
            days_count += 1
            if days_count >= cnt:
                break



    else:
        print(f"Error getting weather data: {response_weather.status_code}")
    return weather_data, city



