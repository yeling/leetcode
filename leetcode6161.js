/*
* auther yeling
* 
* 
*/

/**
 * @param {string} s
 * @return {string}
 */
var removeStars = function(s) {
    let arr = s.split('');
    let res = [];
    let count = 0;
    for(let i = s.length - 1; i >= 0; i--) {
        if(arr[i] == '*') {
            count++;
        } else if(count > 0) {
            count--;
        } else if(count == 0) {
            res.splice(0,0,arr[i])
        }
    }
    return res.join('');
};


s = "leet**cod*e"
// s = "erase*****"
console.log(removeStars(s));
