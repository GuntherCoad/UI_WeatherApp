import requests
from config import API_WEATHER_URL
from location import get_current_location
from flask import (
    Blueprint, render_template, request, 
)

bp = Blueprint('weather', __name__, url_prefix='/weather')
    
@bp.route('/forecast', methods=('GET', 'POST'))
def forecast():
    if request.method == 'POST':
        lati = request.form['latitude']
        long = request.form['longitude']
    else:
        loc_data = get_current_location()
        lati = float(loc_data[0])
        long = float(loc_data[1])
    
    data = get_forecast(lati, long)

    return render_template('forecast.html', data=data)
    

@bp.route('/current', methods=('GET', 'POST'))
def current():
    if request.method == 'POST':
        lati = request.form['latitude']
        long = request.form['longitude']
    else:
        loc_data = get_current_location()
        lati = float(loc_data[0])
        long = float(loc_data[1])

    data = get_current_weather(lati, long)
    
    # Extract temperature in Celsius
    temp_cel = data['current_weather']['temperature']

    # Convert Celsius to Fahrenheit
    temp_fah = temp_cel * 9/5 + 32
 
    # Add to array
    data['current_weather']['temperature_fahrenheit'] = temp_fah

    return render_template('weather.html', data=data)

def get_current_weather(latitude, longitude):
    params = {
    	"latitude":  latitude,
    	"longitude": longitude,
    	"current_weather": "True",
        "temperature_unit": "celsius",
    }
    response = requests.get(API_WEATHER_URL, params=params)
    weather_data = response.json()
    return weather_data
    
def get_forecast(latitude, longitude):
    params = {
    	"latitude":  latitude,
    	"longitude": longitude,
        "temperature_unit": "celsius",
        "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum", "windspeed_10m_max"],
    }
    response = requests.get(API_WEATHER_URL, params=params)
    weather_data = response.json()
    return weather_data
