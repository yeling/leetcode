/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var findSubarrays = function(nums) {
    let cache = new Set();
    for(let i = 1 ; i < nums.length; i++) {
        let sum = nums[i] + nums[i-1];
        if(cache.has(sum)) {
            return true;
        } else {
            cache.add(sum);
        }
    }
    return false;

};

nums = [1,2,3,4,5,0];
console.log(findSubarrays(nums));