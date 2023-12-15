/*
* auther yeling
* 493. 翻转对
* 
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
//暴力模拟
//33 / 138 个通过测试用例
var reversePairs2 = function(nums) {
    let n = nums.length;
    let sum = 0;
    let cache = new Array(n).fill(0);
    for(let i = 0; i < n; i++) {
        cache[i] = 2 * nums[i];
    }
    for(let i = 0; i < n; i++) {
        for(let j = i + 1; j < n; j++) {
            if(nums[i] > cache[j]) {
                sum++;
            }
        }
    }
    return sum;
};

var reversePairs = function(nums) {
    let n = nums.length;
    let sum = 0;
    let cache = new Array(n).fill(0);
    for(let i = 0; i < n; i++) {
        cache[i] = 2 * nums[i];
    }
    for(let i = 0; i < n; i++) {
        for(let j = i + 1; j < n; j++) {
            if(nums[i] > cache[j]) {
                sum++;
            }
        }
    }
    return sum;
};

let nums = [2,4,3,5,1];
console.log(reversePairs2(nums));
console.log(reversePairs(nums));
