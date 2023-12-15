/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var distinctAverages = function(nums) {
    nums.sort((a, b) => a - b);
    let n = nums.length;
    cache = new Set();
    for(let i = 0; i < n / 2; i++) {
        cache.add(nums[i] + nums[n - 1 - i]);
    }
    return cache.size;
};

nums = [4,1,4,0,3,5]
nums = [1,100]

console.log(distinctAverages(nums))
