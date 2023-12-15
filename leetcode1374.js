/*
* auther yeling
* 1374. 生成每种字符都是奇数个的字符串
* 
*/

/**
 * @param {number} n
 * @return {string}
 */
var generateTheString = function(n) {
    let res = new Array(n - 1).fill('a');
    if(n%2 == 0) {
        res.push('b');
    } else {
        res.push('a');
    }
    return res.join('');
};

console.log(generateTheString(3));
// console.log(generateTheString(10));