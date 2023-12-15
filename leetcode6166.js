/*
* auther yeling
* 
* 
*/

/**
 * @param {string} num
 * @return {string}
 */
var largestPalindromic = function (num) {
    let count = new Array(10).fill(0);
    for (let i = 0; i < num.length; i++) {
        count[Number(num.charAt(i))]++;
    }
    //console.log(count);
    //2个一取前缀
    let pre = '';
    let after = '';
    for (let i = 9; i >= 0; i--) {
        if(pre.length == 0 && i == 0) {
            break;
        }
        while (count[i] >= 2) {
            pre += Number(i).toString();
            count[i] -= 2;
        }
    }
    for(let i = pre.length - 1; i >= 0; i--) {
        after += pre.charAt(i);
    }
    //取最后一位
    for (let i = 9; i >= 0; i--) {
        if(count[i] >= 1) {
            pre += Number(i).toString();
            break;
        }
    }
    return pre + after;
};

num = "444947137"
num = "90200009"
console.log(largestPalindromic(num));


