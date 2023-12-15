/*
* auther yeling
* 
* 
*/

/**
 * @param {string} s
 * @return {number}
 */
var partitionString = function(s) {
    let sum = 0;
    let cache = new Set();
    for(let i = 0; i < s.length; i++) {
        //console.log(cache);
        //console.log(sum);
        if(cache.has(s.charAt(i))) {
            cache.clear();
            sum++;
        }
        cache.add(s.charAt(i));
    }
    if(cache.size > 0) {
        sum++;
    }
    return sum;
};

s = "abacaba";
console.log(partitionString(s));
