const apiKEY = "27eedd9e3f839130d3c83e4b0ed69202";
const apiENDPOINT = "api.openweathermap.org"
const weatherResultTemplate = document.getElementById("search-result-template");


/**
 * @description takes parameter limit. This displays "limit" number of locations related to the value in the search box. 
 *              Will eventually link to result page with relevant php info.
 * 
 * @param {*} limit the number of related searches that populate upon typing
 */
function getWeather(limit)
{
    const search = document.getElementById("query");
    const val = search.value;
    
    fetch(`http://api.openweathermap.org/geo/1.0/direct?q=${search.value}&limit=${limit}&appid=${apiKEY}`)
    .then(res => res.json())
    .then(data => {
        data.forEach(element => {
            var card = weatherResultTemplate.content.cloneNode(true).children;
            card.getElementById("data-header").innerHTML = element.name;
            
        });
            
        
    })
    .catch(error => console.error(error));
}
