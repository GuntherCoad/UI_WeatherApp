import requests
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('weather', __name__, url_prefix='/weather')

@bp.route('/current', methods=('GET', 'POST'))
def get_current_temperature(lati, long):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
    	"latitude": lati,
    	"longitude": long,
    	"current_weather": "True",
        "temperature_unit": "fahrenheit",
    }
    error = None
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        current_weather = data.get('current_weather')
        if current_weather:
            current = current_weather['temperature']
        else:
            error = "Current weather data not available"
    else:
        error = "Failed to retrieve data"

    flash(error)
    return render_template('current.html')


latitude = 29.7337
longitude = -98.3728
temperature = get_current_temperature(latitude, longitude)
print(f"Current temperature in San Antonio is: {temperature} F")
