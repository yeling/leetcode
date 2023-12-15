/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countDistinctIntegers = function(nums) {
    let cache = new Set();
    for(let i = 0; i < nums.length; i++) {
        cache.add(nums[i]);
        let temp = nums[i].toString(10);
        let res = '';
        for(let j = 0; j < temp.length; j++) {
            res += temp.charAt(temp.length - 1 - j);
        }
        cache.add(Number(res));
    }
    return cache.size;
};

nums = [1,13,10,12,31]
nums = [1,10,100]
console.log(countDistinctIntegers(nums));