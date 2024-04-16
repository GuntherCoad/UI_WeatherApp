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
});
