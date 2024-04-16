import requests
import sys
from geopy import geocoders
from config import API_WEATHER_URL, GEO_CODE
from location import get_current_location
from flask import (
    Blueprint, render_template, request, 
)

gn = geocoders.GeoNames(username=GEO_CODE)
bp = Blueprint('weather', __name__, url_prefix='/weather')
# TODO: Dynanic loading of card images based on weather_code.    
# {{ # url_for('static', filename='images/weather/' + weather_code + '.svg') }} 
@bp.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        city = request.form['city']
        city, lati, long = get_lat_long(city)

        #lati = request.form['latitude']
        #long = request.form['longitude']
    else:
        loc_data = get_current_location()
        lati = float(loc_data[0])
        long = float(loc_data[1])
        city = gn.reverse((lati, long))[0].split(',')[0]
    
    data = get_forecast(lati, long)
    print(city, file=sys.stderr)
    if data:
        return render_template('overview.html', 
                               today=data, 
                               forecast=data['daily'], 
                               days=data['daily']['time'],
                               city=city, 
                               zip=zip)
    else:
        return "Failed toretrieve data"

@bp.route('/daily', methods=('GET', 'POST'))
def forecast():
    if request.method == 'POST':
        lati = request.form['latitude']
        long = request.form['longitude']
    else:
        loc_data = get_current_location()
        lati = float(loc_data[0])
        long = float(loc_data[1])
    
    data = get_forecast(lati, long)

    if data:
        return render_template('daily.html', forecast=data['daily'], 
                           days=data['daily']['time'], zip=zip)
    else:
        return "Failed toretrieve data"

@bp.route('/today', methods=('GET', 'POST'))
def current():
    if request.method == 'POST':
        lati = request.form['latitude']
        long = request.form['longitude']
    else:
        loc_data = get_current_location()
        lati = float(loc_data[0])
        long = float(loc_data[1])
        city = gn.reverse((lati, long))[0].split(',')[0]

    data = get_forecast(lati, long)
    
    # # Extract temperature in Celsius
    # temp_cel = data['current_weather']['temperature']

    # # Convert Celsius to Fahrenheit
    # temp_fah = temp_cel * 9/5 + 32
 
    # # Add to array
    # data['current_weather']['temperature_fahrenheit'] = temp_fah

    return render_template('today.html', today=data, city=city)

def get_forecast(latitude, longitude):
    params = {
    	"latitude":  latitude,
    	"longitude": longitude,
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
        "current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "is_day", "precipitation", "rain", "showers", "snowfall", "weather_code", "cloud_cover", "pressure_msl", "surface_pressure", "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m"],
        "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum", "windspeed_10m_max"],
    }
    response = requests.get(API_WEATHER_URL, params=params)
    weather_data = response.json()
    return weather_data

def get_lat_long(city):
    place, (lat, long) = gn.geocode(city)
    print("Place:, " + place, file=sys.stderr)
    print("Lat:, " + str(lat), file=sys.stderr)
    print("Long:, " + str(long), file=sys.stderr)
    city = place.split(',')[0]
    # return tuple of lat and long
    return city, lat, long