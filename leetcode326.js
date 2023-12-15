/*
* auther yeling
* 326. 3 的幂
*/
/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function(n) {
    if(n == 1) {
        return true;
    } else if(n == 0) {
        return false;
    } else if(n%3 != 0) {
        return false;
    }
    return isPowerOfThree(n/3);
};

var isPowerOfThree2 = function(n) {
    let all = [ 1,
        3,
        9,
        27,
        81,
        243,
        729,
        2187,
        6561,
        19683,
        59049,
        177147,
        531441,
        1594323,
        4782969,
        14348907,
        43046721,
        129140163,
        387420489,
        1162261467,
        3486784401];
    // let threeSet = new Set();
    // all.forEach((item) => {
    //     threeSet.add(item)
    // })
    
    // let num = 1;
    // while(num < Math.pow(2,32)) {
    //     console.log(num);
    //     threeSet.add(num);
    //     num *= 3;
    // }
    //console.log(threeSet);
    return all.indexOf(n) != -1 ? true : false;
    
};

var isPowerOfThree2 = function(n) {
    //3的19次方的，最大约数
    return n > 0 && 1162261467 % n == 0;
}

let n = 9;
console.log(isPowerOfThree(n));
console.log(isPowerOfThree2(n));