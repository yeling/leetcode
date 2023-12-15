/*
* auther yeling
* 2369. 检查数组是否存在有效划分
* dp问题 
*/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var validPartition = function(nums) {
    let n = nums.length;
    let dp = new Array(n + 1).fill(false);
    dp[0] = true;
    for(let i = 0; i < n; i++) {
        if(i > 0) {
            if(dp[i + 1 - 2]&& nums[i] == nums[i-1]) {
                dp[i+1] = true;
            }
        }
        // 0 1 2
        if(i > 1) {
            if(dp[i + 1 - 3]&& nums[i] == nums[i-1] && nums[i] == nums[i - 2]) {
                dp[i+1] = true;
            }
            if(dp[i + 1 - 3]&& nums[i] == nums[i-1] + 1 && nums[i - 1] == nums[i - 2] + 1) {
                dp[i+1] = true;
            }
        }

    }
    return dp[n];
};

nums = [4,4,4,5,6,7];
console.log(validPartition(nums));


