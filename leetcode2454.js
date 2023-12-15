/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var secondGreaterElement = function(nums) {
    let n = nums.length;
    let stack1 = [];
    let stack2 = [];
    let res = new Array(n).fill(-1);
    for(let i = 0; i < n; i++) {
        while (stack2.length > 0 && nums[i] > nums[stack2[stack2.length - 1]]) {
            res[stack2.pop()] = nums[i];
        }
        let temp = [];
        while (stack1.length > 0 && nums[i] > nums[stack1[stack1.length - 1]]) {
            temp.push(stack1.pop());
        }
        for(let j = temp.length - 1; j >= 0; j--) {
            stack2.push(temp[j]);
        }
        stack1.push(i);
    }
    return res;
};


nums = [2,4,0,9,6]
nums = [11,13,15,12,0,15,12,11,9]
// [15,15,-1,-1,12,-1,-1,-1,-1]
console.log(secondGreaterElement(nums));
