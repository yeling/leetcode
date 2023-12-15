/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
//31 / 33 个通过测试用例
var applyOperations = function (nums) {
    let n = nums.length;
    for (let i = 0; i < n - 1; i++) {
        if (nums[i] == nums[i + 1]) {
            nums[i] = 2 * nums[i];
            nums[i + 1] = 0;
        } else {
            continue;
        }
    }
    // console.log(nums);
    let left = 0, right = 0;
    while (right < n) {
        if (nums[right] != 0) {
            nums[left] = nums[right];
            left++;
            right++;
        } else {
            right++;
        }
    }
    while (left < n) {
        nums[left] = 0;
        left++;
    }
    return nums;
};

// var test = (nums) => {
//     let n = nums.length;
//     let left = 0, right = 0;
//     while (right < n) {
//         if (nums[right] != 0) {
//             nums[left] = nums[right];
//             left++;
//             right++;
//         } else {
//             right++;
//         }
//     }
//     while (left < n) {
//         nums[left] = 0;
//         left++;
//     }
//     return nums;
// }
nums = [0, 2, 0, 2, 0, 0, 1]
nums = [1,2,2,1,1,0]
nums = [0,1]
// console.log(test(nums));
console.log(applyOperations(nums))