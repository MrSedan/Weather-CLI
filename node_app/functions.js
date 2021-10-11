import fetch from 'node-fetch';


const currentWeather = async (city, units="m") => {

    if (city.length > 0 || (units !== "F" && units !== "C"))  {
        let link = '';
        if (units !=="f" && units !=="F") {
            link = `http://api.weatherstack.com/current?access_key=${process.env.API}&query=${city}`
        } else {
            link = `http://api.weatherstack.com/current?access_key=${process.env.API}&units=f&query=${city}`
        } 
        const response = await fetch(link)
        let data = await response.json();
        const weatherInfo = {
            name: data.location.name,
            country: data.location.country,
            region: data.location.region,
            time: data.current.observation_time,
            temperature: data.current.temperature,
            condition: data.current.weather_descriptions[0]
        }

        let weatherText=`
        ${weatherInfo.name} - ${weatherInfo.region} - ${weatherInfo.country}\n
        ###################Info:###################
                  Time: ${weatherInfo.time}                       
                  Condition: ${weatherInfo.condition}             
                  Temperature: ${weatherInfo.temperature} ${units.toLowerCase() === 'f' ? "F°" : "C°"}              
        ###########################################
        `

        console.log(weatherText);
    } else {
        console.log("Error: Write a name of a city or the right value of Units")
    }
   
}

export  {
    currentWeather
}