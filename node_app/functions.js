import fetch from 'node-fetch'; // Импорт функции веб-запроса

// Функция получения погоды
export const currentWeather = async (city, units="m") => {
    // Проверка ввода
    if (city.length > 0 || (units !== "F" && units !== "C" && units !== 'K'))  {
        // Выбор необходимой ссылки в зависимости от выбранной единицы
        const link = `http://api.weatherstack.com/current?access_key=${process.env.API}&${units.toLowerCase()==='f'?'units=f&':''}query=${city}` 
        const response = await fetch(link); // Запрос на API
        let weatherInfo = {};
        // Парсинг ответа от сервера
        try {
            let data = await response.json();
            weatherInfo = {
                name: data.location.name,
                country: data.location.country,
                region: data.location.region,
                time: data.current.observation_time,
                temperature: data.current.temperature + (units.toUpperCase()==='K'?273.15:0),
                condition: data.current.weather_descriptions[0]
            }
        } catch {
            throw new Error('You entered wrong city!')
        }

        // Формирование текста вывода из полученных данных в удобный формат
        let weatherText=`
        ${weatherInfo.name} - ${weatherInfo.region} - ${weatherInfo.country}\n
        ###################Info:###################
                  Time: ${weatherInfo.time}                       
                  Condition: ${weatherInfo.condition}             
                  Temperature: ${weatherInfo.temperature} ${units.toUpperCase()}°              
        ###########################################
        `

        console.log(weatherText);
    } else {
        console.log("Error: Write a name of a city or the right value of Units"); // Вывод ошибки в случае неправильного ввода
    }  
}