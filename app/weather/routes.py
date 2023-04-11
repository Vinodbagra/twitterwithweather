from flask import request, jsonify
from app.weather import weather
from app.weather.controller import get_weather_data



@weather.route('/weather', methods=['GET'])
def get_weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    # Call the get_weather_data() function to retrieve weather data from the API
    weather_data = get_weather_data(lat, lon)
    
    # Extract the relevant information from the API response
    description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']
    
    # Construct a dictionary containing the weather information
    result = {
        'description': description,
        'temperature': temperature,
    }
    
    return jsonify(result)