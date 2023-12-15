/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
//TLE
var goodIndices = function(nums, k) {
    let res = [];
    let n = nums.length;
    for(let i = k; i < n - k; i++) {
        let before = true;
        for(let j = i - k; j < i - 1; j++) {
            if(nums[j] < nums[j+1]) {
                before = false;
                break;
            }
        }

        let after = true;
        for(let j = i + 1; j < i + k; j++) {
            if(nums[j] > nums[j+1]) {
                after = false;
                break;
            }
        }
        if(before && after) {
            res.push(i);
        }    
    }
    return res;
};

nums = [2,1,1,1,3,4,1], k = 2

console.log(goodIndices(nums,k));
