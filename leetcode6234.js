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
var subarrayLCM = function(nums, k) {
    var gcd = function (a, b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }
    let sum = 0;
    for(let i = 0; i < nums.length; i++) {
        let curr = nums[i]
        for(let j = i; j < nums.length; j++) {
            let next = gcd(curr, nums[j]);
            let dst = (curr * nums[j]) / next;
            if(dst == k) {
                console.log(`${i} ${j}`)
                sum++;
            } else if(dst > k) {
                break;
            }
            curr = dst;
        }   
    }
    return sum;

};

nums = [3,6,2,7,1], k = 6
nums = [3], k = 2
nums = [4,6,8], k = 24
nums = [2,1,1,5]
k = 5
console.log(subarrayLCM(nums,k))