import requests
from config import API_WEATHER_URL
from location import get_current_location
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
        loc_data = get_current_location()
        lati = float(loc_data[0])
        long = float(loc_data[1])

        print(lati)
        print(long)

    data = get_current_weather(lati, long)

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
