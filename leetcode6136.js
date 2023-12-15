/*
* auther yeling
* 6136. 算术三元组的数目
* 
*/
/**
 * @param {number[]} nums
 * @param {number} diff
 * @return {number}
 */
var arithmeticTriplets = function (nums, diff) {
    let n = nums.length;
    let sum = 0;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            for (let k = j + 1; k < n; k++) {
                if (nums[k] - nums[j] == diff && nums[j] - nums[i] == diff) {
                    sum++;
                }
            }
        }
    }
    return sum;
}

nums = [4, 5, 6, 7, 8, 9], diff = 2
console.log(arithmeticTriplets(nums, diff));
