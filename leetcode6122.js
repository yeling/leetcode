/*
* auther yeling
* 6122. 使数组可以被整除的最少删除次数
* 
*/

/**
 * @param {number[]} nums
 * @param {number[]} numsDivide
 * @return {number}
 */
//37 / 39 个通过测试用例
//加个缓存，直接过了
var minOperations = function (nums, numsDivide) {
    //console.log(nums);
    nums.sort((a, b) => a - b);
    let cache = new Map();
    //console.log(nums);
    let count = 0, find = false;
    for (let i = 0; i < nums.length; i++) {
        if(cache.get(nums[i]) == false) {
            count++;
            continue;
        }
        find = true;
        for (let j = 0; j < numsDivide.length; j++) {
            if (numsDivide[j] % nums[i] != 0) {
                find = false;
                break;
            }
        }
        if (find) {
            return count;
        }
        count++;
        cache.set(nums[i],false);
    }
    return -1;
};

nums = [2, 3, 2, 4, 3], numsDivide = [9, 6, 9, 3, 15];
// nums = [4,3,6], numsDivide = [8,2,6,10];
console.log(minOperations(nums, numsDivide));