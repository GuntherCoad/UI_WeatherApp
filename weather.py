import requests
import sys
from geopy import geocoders
from config import API_WEATHER_URL, GEO_CODE
from location import get_current_location
from datetime import datetime as dt
from flask import (
    Blueprint, render_template, request, 
)

gn = geocoders.GeoNames(username=GEO_CODE)
bp = Blueprint('weather', __name__, url_prefix='/weather')

#global city variable
loc_data = get_current_location()
lati = float(loc_data[0])
long = float(loc_data[1])
city = gn.reverse((lati, long))[0].split(',')[0]
navdate = dt.now().strftime("%m/%d/%Y")
#global data array for weather
data = {}


# TODO: Dynanic loading of card images based on weather_code.    
# {{ # url_for('static', filename='images/weather/' + weather_code + '.svg') }} 
@bp.route('/', methods=('GET', 'POST'))
def home():
    global city, lati, long, data

    if request.method == 'POST':
        city = request.form['city']
        city, lati, long = get_lat_long(city)
  
    data = get_forecast(lati, long)
    print(city, file=sys.stderr)
    if data:
        return render_template('overview.html', 
                               today=data, 
                               forecast=data['daily'], 
                               days=data['daily']['time'],
                               city=city, 
                               dow=data['daily']['day_of_week'],
                               navdate=navdate,
                               zip=zip)
    else:
        return "Failed toretrieve data"

@bp.route('/daily', methods=('GET', 'POST'))
def forecast():
    global lati, long, data
    if request.method == 'POST':
        lati = request.form['latitude']
        long = request.form['longitude']
    
    data = get_forecast(lati, long)

    if data:
        return render_template('daily.html', forecast=data['daily'], 
                           days=data['daily']['time'], navdate=navdate, zip=zip)
    else:
        return "Failed toretrieve data"

@bp.route('/today', methods=('GET', 'POST'))
def current():
    global lati, long, data, city
    if request.method == 'POST':
        lati = request.form['latitude']
        long = request.form['longitude']

    data = get_forecast(lati, long)
    
    # # Extract temperature in Celsius
    # temp_cel = data['current_weather']['temperature']

    # # Convert Celsius to Fahrenheit
    # temp_fah = temp_cel * 9/5 + 32
 
    # # Add to array
    # data['current_weather']['temperature_fahrenheit'] = temp_fah

    return render_template('today.html', today=data, city=city, navdate=navdate)

def get_forecast(latitude, longitude):
    params = {
    	"latitude":  latitude,
    	"longitude": longitude,
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
        "current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "is_day", "precipitation", "rain", "showers", "snowfall", "weather_code", "cloud_cover", "pressure_msl", "surface_pressure", "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m"],
        "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum", "windspeed_10m_max", "weather_code"],
    }
    response = requests.get(API_WEATHER_URL, params=params)
    weather_data = response.json()
    convert_date(weather_data)
    add_day_of_week(weather_data)
    print(weather_data)
    return weather_data

def convert_date(data):
    for i in range(len(data['daily']['time'])):
        og_date = data['daily']['time'][i]
        new_date = dt.strptime(og_date, "%Y-%m-%d").strftime("%m/%d/%Y")
        data['daily']['time'][i] = new_date

def add_day_of_week(data):
    data['daily']['day_of_week'] = []
    for date_str in data['daily']['time']:
        date = dt.strptime(date_str, '%m/%d/%Y')
        day_of_week = date.strftime('%A')
        data['daily']['day_of_week'].append(day_of_week)

def get_lat_long(city):
    place, (lat, long) = gn.geocode(city)
    print("Place:, " + place, file=sys.stderr)
    print("Lat:, " + str(lat), file=sys.stderr)
    print("Long:, " + str(long), file=sys.stderr)
    city = place.split(',')[0]
    # return tuple of lat and long
    return city, lat, long
