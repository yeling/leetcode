/*
* auther yeling
* 
* 462. 最小操作次数使数组元素相等 II
* 中位数，贪心可以证明
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minMoves2 = function(nums) {
    nums.sort((a,b) => a - b);
    let target = nums[Math.floor(nums.length/2)];
    let sum = 0;
    for(let i = 0; i < nums.length; i++) {
        sum += Math.abs(nums[i] - target);
    }
    return sum;
};


nums = [1,10,2,9]
console.log(minMoves2(nums));