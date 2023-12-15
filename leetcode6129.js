/*
* auther yeling
* 
* 
*/

var zeroFilledSubarray = function (nums) {
    let sum = 0;
    let count = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] == 0) {
            count++;
        } else {
            sum += count * (count + 1) / 2;
            count = 0;
        }
    }
    if(count != 0) {
        sum += count * (count + 1) / 2;
    }
    return sum;
};

nums = [1, 3, 0, 0, 2, 0, 0, 4];
nums = [0,0,0,2,0,0];

console.log(zeroFilledSubarray(nums));