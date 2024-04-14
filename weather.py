import requests
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('weather', __name__, url_prefix='/weather')
    
@bp.route('/current', methods=('GET', 'POST'))
def current():
    if request.method == 'POST':
        lati = request.form['latitude']
        long = request.form['longitude']
    else:
        lati = 0
        long = 0

    data = get_current_weather(lati, long)

    return render_template('weather.html', data=data)

def get_current_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
    	"latitude":  latitude,
    	"longitude": longitude,
    	"current_weather": "True",
        "temperature_unit": "fahrenheit",
        "temperature_unit": "celsius",
    }
    response = requests.get(url, params=params)
    weather_data = response.json()
    return weather_data
    # return render_template('weather.html', weather_data=weather_data)
