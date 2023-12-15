/*
* auther yeling
* 2009. 使数组连续的最少操作数
* 
*/

/**
 * @param {number[]} nums
 * @return {number}
*/
var minOperations = function(nums) {
    //滑动窗口，元素区间为K，个数为N，
    //以N为窗口大小，找到存在最多的元素的窗口，去重
    nums.sort((a,b) => a - b);
    let max = 0;
    let n = nums.length;
    let left = 0, right = 0;
    let cache = new Set();
    while(right < n) {
        if(nums[right] - nums[left] < n) {
            cache.add(nums[right]);
            max = Math.max(max, cache.size);
            right++;            
        } else {
            cache.delete(nums[left]);
            left++;
        }
        //console.log(max)
    }
    return n - max;
};

// nums = [1,2,3,5,6];
// nums = [1,10,100,1000];
nums = [8,5,9,9,8,4];
console.log(minOperations(nums));

