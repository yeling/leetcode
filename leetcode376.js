/*
376. 摆动序列
https://leetcode.cn/problems/wiggle-subsequence/
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
 var wiggleMaxLength = function(nums) {
    let cache = [[],[]];
    const n = nums.length;
    let ret = 1;
    
    cache[0] = new Array(n).fill(0);
    cache[1] = new Array(n).fill(0);
    
    cache[0][0] = 1;
    cache[0][1] = 0;
    for(let i = 1; i < nums.length; i++) {
        for(let j = i - 1; j >= 0; j--) {
            if(nums[i] > nums[j]) {
                if(cache[1][j] == 0 || cache[1][j] == 2) {
                    cache[0][i] = cache[0][j] + 1;
                    cache[1][i] = 1;
                    break;
                } 
            } else if(nums[i] < nums[j]) {
                if(cache[1][j] == 0 || cache[1][j] == 1) {
                    cache[0][i] = cache[0][j] + 1;
                    cache[1][i] = 2; 
                    break;
                } 
            } else if(nums[i] == nums[j]) {
                cache[0][i] = cache[0][j];
                cache[1][i] = cache[1][j];
            }
        }
        ret = Math.max(ret,cache[0][i]);
        console.log(`${i} ${cache[0]}`)
    }
    return ret;
};

let nums = [1,17,5,10,13,15,10,5,16,8];
nums = [3,3,3,2,5];
console.log(`${wiggleMaxLength(nums)}`)