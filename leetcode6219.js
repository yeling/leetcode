/*
* auther yeling
* 
* 
*/

/**
 * @param {number} num
 * @return {boolean}
 */
var sumOfNumberAndReverse = function(num) {
    let reverse = (a) => {
        let temp = a.toString(10);
        let res = '';
        for(let j = 0; j < temp.length; j++) {
            res += temp.charAt(temp.length - 1 - j);
        }
        return Number(res);
    }
    //console.log(reverse(140));
    for(let i = 0; i <= num; i++) {
        if(i + reverse(i) == num) {
            return true;
        }
    }
    return false;
};

num = 181
num = 443
num = 63
console.log(sumOfNumberAndReverse(num));