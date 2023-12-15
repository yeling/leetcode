/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
 var findMaxK = function(nums) {
    //
    let max = -1;
    let cache = new Set();
    for(let i = 0; i < nums.length; i++) {
        if(cache.has(-nums[i])) {
            max = Math.max(max, Math.abs(nums[i]));
        }
        cache.add(nums[i]);
    }
    return max;
};

nums = [-1,10,6,7,-7,1]
nums = [-10,8,6,7,-2,-3]
console.log(findMaxK(nums));