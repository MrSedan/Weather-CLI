// Импортирование необходимых библиотек
import program from 'commander';
import dotenv from 'dotenv';

// Импортирование функции из другого файла
import { currentWeather } from './functions.js';

dotenv.config({path: '../.env'}) // Получение API ключа из файла .env




program.version("1.0.0").description("Console Application for find the Weather of a city"); // Информация о программе

// Информация и запуске программы с флагами
program
    .command('current <city> <units>')
    .alias('c')
    .description('See the weather of the city, write F to get temperature in Fahrenheit, or C to get in Celcius, or K to get in Kelvin')
    .action((city, units) => currentWeather(city, units.toLowerCase()))

// Получение аргументов запуска
program.parse(process.argv);
