import fetch from "node-fetch"; // Импорт функции веб-запроса

// Функция получения погоды
export const currentWeather = async (city, units = "m") => {
  // Проверка ввода
  if (city.length > 0 && !(units !== "f" && units !== "c" && units !== "k")) {
    // Выбор необходимой ссылки в зависимости от выбранной единицы
    const link = `http://localhost:5000/get-weather/${units}/${city}`;
    const response = await fetch(link); // Запрос на API
    if (response.status != 200) {
      const data = await response.json()
      throw new Error(data.detail)
    }
    let weatherInfo = {};
    // Парсинг ответа от сервера
    try {
      let data = await response.json();
      weatherInfo = {
        name: data.name,
        country: data.country,
        region: data.region,
        time: data.time,
        temperature:
          data.temperature,
        condition: data.condition,
      };
    } catch {
      throw new Error("You entered wrong city!");
    }

    // Формирование текста вывода из полученных данных в удобный формат
    let weatherText = `
        ${weatherInfo.name} - ${weatherInfo.region} - ${weatherInfo.country}\n
        ###################Info:###################
                  Time: ${weatherInfo.time}                       
                  Condition: ${weatherInfo.condition}             
                  Temperature: ${
                    weatherInfo.temperature
                  } ${units.toUpperCase()}°              
        ###########################################
        `;

    console.log(weatherText);
  } else {
    console.log("Error: Write a name of a city or the right value of Units"); // Вывод ошибки в случае неправильного ввода
  }
};
