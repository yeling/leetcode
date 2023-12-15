/*
* auther yeling
* 
* 
*/

/**
 * @param {number} celsius
 * @return {number[]}
 */
 var convertTemperature = function(celsius) {
    //摄氏度 + 273.15
    //摄氏度 * 1.80 + 32.00
    return [celsius + 273.15, celsius * 1.80 + 32.00]

};

celsius = 36.50
console.log(convertTemperature(celsius))

