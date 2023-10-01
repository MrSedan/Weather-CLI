import fetch from 'node-fetch'; // Импорт функции веб-запроса

// Функция получения погоды
const currentWeather = async (city, units="m") => {
    // Проверка ввода
    if (city.length > 0 || (units !== "F" && units !== "C"))  {
        let link = '';
        
        // Выбор необходимой ссылки в зависимости от выбранной единицы
        if (units !=="f" && units !=="F") {
            link = `http://api.weatherstack.com/current?access_key=${process.env.API}&query=${city}`
        } else {
            link = `http://api.weatherstack.com/current?access_key=${process.env.API}&units=f&query=${city}`
        } 
        const response = await fetch(link); // Запрос на API

        // Парсинг ответа от сервера
        let data = await response.json();
        const weatherInfo = {
            name: data.location.name,
            country: data.location.country,
            region: data.location.region,
            time: data.current.observation_time,
            temperature: data.current.temperature,
            condition: data.current.weather_descriptions[0]
        }

        // Формирование текста вывода из полученных данных в удобный формат
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
        console.log("Error: Write a name of a city or the right value of Units"); // Вывод ошибки в случае неправильного ввода
    }
   
}

// Разрешение на использование функции в другом файле
export  {
    currentWeather
}