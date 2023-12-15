/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minMoves = function(nums) {
    let min = Number.MAX_SAFE_INTEGER;
    for(let i = 0; i < nums.length; i++) {
        if(min > nums[i]) {
            min = nums[i];
        }
    }
    let sum = 0;
    for(let i = 0; i < nums.length; i++) {
        sum += nums[i] - min;
    }
    return sum;

};
nums = [1,2,3];
nums = [1,1,1];
console.log(minMoves(nums));
