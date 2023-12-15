/*
* auther yeling
* 
* 
*/
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximumSubarraySum = function(nums, k) {
    let n = nums.length;
    let left = 0, right = 0;
    let maxSum = 0;
    let curSum = 0;
    let cache = new Map();
    let preSum = new Array(n + 1).fill(0);
    for(let i = 0; i < n; i++) {
        preSum[i + 1] = preSum[i] + nums[i];
    }
    while(right < n) {
        let item = cache.get(nums[right]);
        if(item == null) {
            cache.set(nums[right], right);
            if(right - left + 1 == k) {
                curSum = preSum[right + 1] - preSum[left];
                maxSum = Math.max(maxSum, curSum);
                cache.delete(nums[left]);
                left++;
            }
            right++;
        } else {
            for(let i = left; i <= item; i++) {
                cache.delete(nums[i]);
            }
            left = item + 1;
            cache.set(nums[right], right);
            right++;
        }
        
    }
    return maxSum;
};

nums = [1,5,4,2,9,9,9], k = 3
nums = [4,4,4], k = 3
nums = [9,9,9,1,2,3]
k = 3
console.log(maximumSubarraySum(nums,k))
