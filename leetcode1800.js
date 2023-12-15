/*
* auther yeling
* 1800. 最大升序子数组和
* 
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAscendingSum = function(nums) {
    let last = nums[0];
    let tempSum = nums[0];
    let maxSum = nums[0];
    for(let i = 1; i < nums.length; i++) {
        if(nums[i] > last) {
            tempSum += nums[i];
            last = nums[i];
            maxSum = Math.max(maxSum, tempSum);
        } else {
            tempSum = nums[i];
            last = nums[i];
            maxSum = Math.max(maxSum, tempSum);
        }
    }
    return maxSum;

};

nums = [10,20,30,5,10,50];
nums = [100,10,1]
console.log(maxAscendingSum(nums));