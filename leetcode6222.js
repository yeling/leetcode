/*
* auther yeling
* 
* 
*/

/**
 * @param {number} n
 * @param {number} target
 * @return {number}
 */
var makeIntegerBeautiful2 = function(n, target) {
    let calc = (num) => {
        let sum = 0;
        while(num > 0) {
            sum += num%10;
            num = Math.floor(num/10);
        }
        return sum;
    }
    let ret = 0;
    while(true) {
        let curr = calc(n + ret)
        if(curr <= target) {
            break;
        }
        ret++;
        //console.log(`${curr} ${ret}`);
    }
    return ret;
};

var makeIntegerBeautiful = function(n, target) {
    let str = ('' + n).split('').map((value) => Number(value));
    str.splice(0,0,0);
    //console.log(str);
    let sum = 0;
    while(true) {
        sum = 0;
        for(let i = 0; i < str.length; i++) {
            sum += str[i];
        }
        if(sum <= target) {
            break;
        }

        let index = str.length - 1;
        while(str[index] == 0) {
            index--;
        }
        str[index] = 0;
        for(let i = index - 1; i >= 0; i--) {
            str[i]++;
            if(str[i] == 10) {
                str[i] = 0;
            } else {
                break;
            }
        }
    }
    let ret = Number(str.join('')) - n;
    return ret;
};

n = 16, target = 6
// n = 6870000, target = 25
console.log(makeIntegerBeautiful2(n, target));
console.log('makeIntegerBeautiful')
console.log(makeIntegerBeautiful(n, target));


