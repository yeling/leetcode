/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarrayGCD = function(nums, k) {
    let gcd = function (a, b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    let sum = 0;
    let n = nums.length;
    for(let i = 0; i < n; i++) {
        if(nums[i] % k != 0) {
            continue;
        }
        for(let j = i; j < n; j++) {
            if(nums[j] % k != 0) {
                break;
            }
            let curr = nums[i];
            for(let m = i + 1; m <= j; m++) {
                curr = gcd(curr, nums[m]);
                if(curr < k) {
                    break;
                }
            }
            if(curr == k) {
                sum++;
            }
        }
    }
    return sum;

};

nums = [9,3,1,2,6,3], k = 3
nums = [4], k = 7
console.log(subarrayGCD(nums, k));