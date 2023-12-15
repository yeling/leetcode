/*
* auther yeling
* 
* 1403. 非递增顺序的最小子序列
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var minSubsequence = function(nums) {
    nums.sort((a,b) => b - a);
    let sum = 0;
    nums.forEach((item) => {
        sum += item;
    })
    let curr = 0;
    let res = [];
    let index = 0;
    let dst = Math.floor(sum/2);
    while(curr <= dst) {
        curr += nums[index];
        res.push(nums[index]);
        index++;
    }
    return res;
};

nums = [4,3,10,9,8]
nums = [1,3,2,3,1]
console.log(minSubsequence(nums));