/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} target
 * @param {number[]} arr
 * @return {boolean}
 */
var canBeEqual = function(target, arr) {
    let n = target.length;
    target.sort((a,b) => a - b);
    arr.sort((a,b) => a - b);
    for(let i = 0; i < n; i++) {
        if(target[i] != arr[i]) {
            return false;
        }
    }
    return true;
};

target = [3,7,9], arr = [3,7,11]
console.log(canBeEqual(target,arr));