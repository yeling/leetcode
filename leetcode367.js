/*
* auther yeling
* 367. 有效的完全平方数
* 
*/

/**
 * @param {number} num
 * @return {boolean}
 */
//5% 5%
var isPerfectSquare = function(num) {
    if(num == 1) {
        return true;
    }
    let i = Math.floor(num/2);
    while(i*i > num) {
        //console.log(i);
        i--;
    }
    if(i * i == num) {
        return true;
    }
    return false;
};


console.log(`${isPerfectSquare(28)}`);
console.log(`${isPerfectSquare(16)}`);