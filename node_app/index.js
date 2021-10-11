import program from 'commander';
import dotenv from 'dotenv';


import {currentWeather} from './functions.js'
dotenv.config({path: '../.env'})




program.version("1.0.0").description("Console Application for find the Weather of a city");
program
    .command('current <city> <units>')
    .alias('c')
    .description('See the weather of the city, write F to get temperature in Fahrenheit, or C to get in Celcius')
    .action((city, units) => currentWeather(city, units))


program.parse(process.argv);
