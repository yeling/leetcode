/*
* auther yeling
* 
* 
*/

/**
 * @param {string} s
 * @return {number}
 */
var longestContinuousSubstring = function(s) {
    let max = 1;
    let temp = 1;
    for(let i = 1; i < s.length; i++) {
        if(s.charCodeAt(i) - s.charCodeAt(i - 1) == 1) {
            temp++;
            max = Math.max(max, temp);
        } else {
            temp = 1;
        }
    }
    return max;
};

s = "acde"
console.log(longestContinuousSubstring(s));