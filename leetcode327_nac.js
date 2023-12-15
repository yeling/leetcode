/*
* auther yeling
* 327. 区间和的个数
* 前缀和
*/
/**
 * @param {number[]} nums
 * @param {number} lower
 * @param {number} upper
 * @return {number}
 */
//64 / 67 个通过测试用例，超时了
/*
*先求前缀和，然后n2，循环检查区间是否满足要求
*/
var countRangeSum = function(nums, lower, upper) {
    let preSum = new Array(nums.length + 1);
    preSum.fill(0);
    for(let i = 1; i <= nums.length; i++) {
        preSum[i] = nums[i - 1] + preSum[i-1];
    }
    let count = 0;
    for(let i = 1; i < nums.length + 1; i++) {
        for(let j = i; j < nums.length + 1; j++) {
            let temp = preSum[j] - preSum[i - 1];
            if(temp >= lower && temp <= upper) {
                count++;
            }
        }
    }
    return count;

};


var countRangeSum2 = function(nums, lower, upper) {
    let preSum = new Array(nums.length + 1);
    preSum.fill(0);
    for(let i = 1; i <= nums.length; i++) {
        preSum[i] = nums[i - 1] + preSum[i-1];
    }
    let count = 0;
    for(let i = 1; i < nums.length + 1; i++) {
        for(let j = i; j < nums.length + 1; j++) {
            let temp = preSum[j] - preSum[i - 1];
            if(temp >= lower && temp <= upper) {
                count++;
            }
        }
    }
    return count;

};

// let nums = [-2,5,-1], lower = -2, upper = 2;
let nums = [0], lower = 0, upper = 0;
console.log(`${countRangeSum(nums,lower,upper)}`);

