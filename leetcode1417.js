/*
* auther yeling
* 
* 
*/

/**
 * @param {string} s
 * @return {string}
 */
var reformat = function(s) {
    let nums = new Array();
    let letters = new Array();
    
    for(let i = 0 ; i < s.length; i++) {
        if(isNaN(s.charAt(i))) {
            letters.push(s.charAt(i));
        } else {
            nums.push(s.charAt(i));
        }
    } 
    if(Math.abs(nums.length - letters.length) > 1) {
        return '';
    }
    let res = '';
    let len = Math.min(nums.length,letters.length);
    for(let i = 0; i < len; i++) {
        res += nums[i] + letters[i];
    }
    if(nums.length < letters.length) {
        res = letters.pop() + res;
    } else if(nums.length > letters.length) {
        res = res + nums.pop();
    }
    return res;
};
s = "a0b1c2";
s = "covid2019";

console.log(s);
console.log(reformat(s));