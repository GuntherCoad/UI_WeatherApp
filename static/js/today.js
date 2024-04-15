console.log("hello");

document.addEventListener('DOMContentLoaded', function() {
    // var tempEl = document.getElementById('today-temp');
    var codeEl= document.getElementById('today-code');

    // var temp = parseFloat(tempEl.textContent.trim());
    var wcode = parseInt(codeEl.textContent.trim());

    // console.log(temp);
    console.log(wcode);

    var imgEl= document.getElementById('image');
    if (wcode == 0) {
        imgEl.src = '/static/images/cloudy.png';
    } else {
        imgEl.src = '/static/images/rain.png';
    }
});
