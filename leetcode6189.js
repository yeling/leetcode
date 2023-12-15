/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    let max = 0;
    let maxLen = 0;
    let currLen = 0;
    for(let i = 0; i < nums.length; i++) {
        if(max < nums[i]) {
            max = nums[i];
            currLen = 1;
            maxLen = currLen;
        } else if(max == nums[i]) {
            currLen++;
            maxLen = Math.max(maxLen, currLen);
        } else {
            currLen = 0;
        }
    }
    return maxLen;
};

nums = [1,2,3,4];
// nums = [311155,311155,311155,311155,311155,311155,311155,311155,201191,311155]

nums = [96317,96317,96317,96317,96317,96317,96317,96317,96317,279979]
console.log(longestSubarray(nums));