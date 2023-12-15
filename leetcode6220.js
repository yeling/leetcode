/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
 var averageValue = function(nums) {
    let sum = 0;
    let count = 0;
    for(let i = 0; i < nums.length; i++) {
        if(nums[i]%3 == 0 && nums[i]%2 == 0) {
            sum += nums[i];
            count++;
        }
    }
    let ret = 0;
    if(count > 0) {
        ret = Math.floor(sum/count);
    }
    return ret;
};

nums = [1,3,6,10,12,15]
nums = [1,2,4,7,10]
nums = [9,3,8,4,2,5,3,8,6,1]
console.log(averageValue(nums));