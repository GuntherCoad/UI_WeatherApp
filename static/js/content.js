const apiKEY = "27eedd9e3f839130d3c83e4b0ed69202";
const apiENDPOINT = "api.openweathermap.org"

const query = document.getElementById("query");
const resultbox = document.getElementById("results");
const searchButton = document.getElementById("querySearch");

/**
 * @description takes parameter limit. This displays "limit" number of locations related to the value in the search box. 
 *              Will eventually link to result page with relevant php info.
 * 
 * @param {*} limit the number of related searches that populate upon typing
 */
function getSearchResults(limit)
{
    const search = document.getElementById("query");
    const val = search.value;
    
    fetch(`http://api.openweathermap.org/geo/1.0/direct?q=${search.value}&limit=${limit}&appid=${apiKEY}`)
    .then(res => res.json())
    .then(data => {
        displayResult(data);
        //console.log(data);
      
    })
    .catch(error => console.error(error));
}

/**
 * @description displays the search results of the getSearchResults() method. result is turned into an array that is filtered based on country(US).
 * 
 * @param {*} result The json list of relevant search items from the api response.
 */
function displayResult(result) {
    var iterat = 0;
    const content = result.flatMap((list)=> {
        
        if(list.country.match(/US/))            //matching US country code
        {
            //console.log(list);
            //setAPICall(list.lon, list.lat)
            iterat++;
            const resultHTML =  "<li id=" + `item${iterat}` + "><button>" + list.name + ", " + list.state + " </button></li>";
            return resultHTML;
        }
        else
            return [];
    });

    //document.getElementById(`item${iterat - 1}`).setAttribute("onclick", "setAPICall(" + `${list.lon},${list.lat}` + ")");
    //code snippet needs to be looped outside of content
    //prob in if statement

    if(content.length > 0)
    {
        resultbox.innerHTML = "<ul>" + content.join("") + "</ul>";
        for(i = 0; i < 5; i++)
        {
            const currItem = document.getElementById(`item${i}`);
            if(currItem == null)
            {
                continue;
            }
            else
            {
                currItem.setAttribute("onclick","setAPICall(" + `${content[i].lon},${content[i].lat}` + ")")
            }
        }
    }
    else
        resultbox.innerHTML = "";
}

/**
 * @description grabs the information for the API call from within displayResult(). Will be used when selecting one of the search results to display.
 * @requires function displayResult()
 */
function setAPICall(lon, lat)
{
    fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKEY}&units=imperial`)
    .then(res => res.json())
    .then(data => {
        //log(data);
      
    })
    .catch(error => console.error(error));
}

/**
 * @description Hides the home page elements and displays the result page elements upon pressing the submit button.
 */
function onSearch() {
    const homeElem = document.getElementsByClassName("home");
    const resultElem = document.getElementsByClassName("result-weather");
    for (const element of homeElem) {
        element.setAttribute("style", "display: none");
    }
    for(const element of resultElem) {
        element.setAttribute("style", "display:block");
    }
}
    

query.addEventListener('keyup', function () {
    getSearchResults(5);
}, 'false');

searchButton.addEventListener('click', function() {
    onSearch();
}, "false");
