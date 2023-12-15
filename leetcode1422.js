/*
* auther yeling
* 1422. 分割字符串的最大得分
* 
*/

/**
 * @param {string} s
 * @return {number}
 */
//96 / 104
var maxScore = function (s) {
    let n = s.length;
    let preZero = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        preZero[i + 1] = preZero[i];
        if (s.charAt(i) == 0) {
            preZero[i + 1] = preZero[i] + 1;
        }
    }
    preZero.shift();

    let max = 0;
    for (let i = 0; i < n - 1; i++) {
        let curr = preZero[i] + (n - 1 - i - (preZero[n - 1] - preZero[i]))
        max = Math.max(max,curr);
    }

    console.log(preZero);
    return max;
};

s = "011101"
s = "00111"
s = "00"
console.log(maxScore(s));
