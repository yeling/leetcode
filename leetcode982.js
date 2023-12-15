/*
* auther yeling
* 982. 按位与为零的三元组
* 
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countTriplets = function(nums) {
    let n = nums.length;
    let sum = 0;
    for(let i = 0; i < n; i++) {
        if(nums[i] == 0) {
            sum += n * n;
            continue;
        }
        for(let j = 0; j < n; j++) {
            if((nums[i] & nums[j]) == 0) {
                sum += n;
                continue;
            }
            for(let k = 0; k < n; k++) {
                if((nums[i] & nums[j] & nums[k]) == 0) {
                    sum++;
                }
            }
        }

    }
    return sum;

};

let nums = [2,1,3];
 nums = [0,0,0];
console.log(countTriplets(nums))