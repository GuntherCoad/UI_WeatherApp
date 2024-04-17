const apiKEY = "27eedd9e3f839130d3c83e4b0ed69202";



function pyLoadHourly(city, lat, lon) {
    fetch(`https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=${lat}&lon=${lon}&appid=${apiKEY}&cnt=12`)
    .then(res => res.json())
    .then(data => {
        var content = [];
        var hourlyArr = [];
        const hourlyDisplay = document.getElementById('hourly-view')
        content = data.list;
        for(element in content)
        {
            const currElem = content[element];
            const elemUnix = timeConverter(currElem.dt);
            console.log(content[element]);
            const foreCastCard =`   <div class="card col-1">
                                    <div class="card-body"></div>
                                    <div class="card-body">${elemUnix}</div>
                                    <div class="card-body">${currElem.weather[0].description}</div></div>`;
            hourlyArr.push(foreCastCard);
        }
        hourlyDisplay.innerHTML = hourlyArr.join(""); 
    })
    .catch(error => console.error(error));
}

document.addEventListener('DOMContentLoaded', function() {
    // var tempEl = document.getElementById('today-temp');
    var codeEl= document.getElementById('today-code');
    var isDayEl= document.getElementById('isDay');

    // var temp = parseFloat(tempEl.textContent.trim());
    var wcode = parseInt(codeEl.textContent.trim());
    var is_day= parseInt(isDayEl.textContent.trim());

    // console.log(temp);
    console.log(wcode);
    console.log(is_day);

    var imgEl= document.getElementById('image');
    const cityName = document.getElementById('pyCity');
    const lat = document.getElementById('latitude').textContent;
    const lon = document.getElementById('longitude').textContent;
    console.log(cityName.innerText + ', lat: ' + lat + ' , lon: ' + lon);

    switch (wcode) {
        case 1:
        case 2:
        case 3:
            if (is_day == 0) {
                imgEl.src = '/static/images/fill/darksky/clear-night.svg';
            }
            else {
                imgEl.src = '/static/images/fill/darksky/clear-day.svg';
            }
            break;
        case 45:
        case 48:
            imgEl.src = '/static/images/fill/darksky/fog.svg';
            break;
        case 51:
        case 53:
        case 55:
        case 56:
        case 57:
            imgEl.src = '/static/images/fill/darksky/drizzle.svg';
            break;
        case 61:
        case 63:
        case 65:
        case 66:
        case 67:
            imgEl.src = '/static/images/fill/darksky/rain.svg';
            break;
        case 71:
        case 73:
        case 75:
        case 77:
            imgEl.src = '/static/images/fill/darksky/snow.svg';
            break;
        default:
            imgEl.src = '/static/images/fill/darksky/clear-day.svg';
    }
    pyLoadHourly(cityName, lat, lon);
});

function timeConverter(UNIX_timestamp){
    var a = new Date(UNIX_timestamp * 1000);
    var time = a.toLocaleTimeString('en-US', {timeStyle: "short"});
    return time;
  }
  
  function loadHourlyWeather(lat, lon) {
    fetch(`https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=${lat}&lon=${lon}&appid=${apiKEY}&cnt=5`)
    .then(res => res.json())
    .then(data => {
        var content = [];
        var forecastArr = [];
        const forDisplay = document.getElementById("forecastDisplay");
        content = data.list;
        for(element in content)
        {
            const currElem = content[element];
            const elemUnix = timeConverter(currElem.dt);
            console.log(content[element]);
            const foreCastCard =`   <div class="card col-1">
                                    <div class="card-body">${setWeatherIcon(currElem.weather[0].id)}</div>
                                    <div class="card-body">${elemUnix}</div>
                                    <div class="card-body">${currElem.weather[0].description}</div></div>`;
            forecastArr.push(foreCastCard);
        }
        forDisplay.innerHTML = forecastArr.join("");
      
    })
    .catch(error => console.error(error));
}