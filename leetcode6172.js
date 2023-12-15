/*
* auther yeling
* 
* 
*/

/**
 * @param {number} n
 * @return {boolean}
 */
var isStrictlyPalindromic = function(n) {
    for(let i = 2; i <= n - 2; i++) {
        let curr = calcN(n,i);
        //console.log(curr);
        if(isHuiwen(curr) == false) {
            return false;
        }
    }
    return true;
};

var calcN = (n,b) => {
    let res = '';
    while(n > 0) {
        res = n%b + res;
        n = Math.floor(n / b);
    }
    return res;
}

var isHuiwen = function (temp) {
    //console.log(`isHuiwen ${temp}`)
    let left = 0, right = temp.length - 1;
    while (left < right) {
        if (temp.charAt(left) != temp.charAt(right)) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

n = 4;
console.log(isStrictlyPalindromic(n));