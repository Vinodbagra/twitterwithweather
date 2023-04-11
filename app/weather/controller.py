import requests
from flask import current_app

def get_weather_data(lat, lon):
    """
    Makes a GET request to the OpenWeatherMap API to retrieve weather data for the given latitude and longitude.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=09808204c046b6c1b24a0b41458fb578"
    response = requests.get(url)
    data = response.json()
    return data