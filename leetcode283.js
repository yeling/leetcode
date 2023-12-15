//283. 移动零
//双指针问题
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let left = 0, right = 0;
    while(right < nums.length && left < nums.length) {
        //left找到第一个0
        if(nums[left] != 0) {
            left++;
        } else {
            //left == 0
            right = left;
            while(right < nums.length) {
                if(nums[right] == 0) {
                    right++;
                } else {
                    nums[left] = nums[right];
                    nums[right] = 0;
                    left++;
                    break;
                }
            }
        } 
    }
    return nums;
};

var moveZeroes1 = function(nums) {
    let left = 0, right = 0;
    while(right < nums.length && left < nums.length) {
        //left找到第一个0
        if(nums[left] != 0) {
            left++;
        } else {
            //left == 0
            if(right == 0) {
                right = left;
            }
            while(right < nums.length) {
                if(nums[right] == 0) {
                    right++;
                } else {
                    nums[left] = nums[right];
                    nums[right] = 0;
                    left++;
                    break;
                }
            }
        } 
    }
    return nums;
};

let nums = [0,1,0,3,12];
console.log(nums);
console.log(moveZeroes(nums));
nums = [0,1,0,3,12];
console.log(moveZeroes1(nums));