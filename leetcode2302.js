/*
* auther yeling
* 2302. 统计得分小于 K 的子数组数目
* 
*/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
//TLE
//153 / 167 个通过测试用例
var countSubarrays2 = function (nums, k) {
    let n = nums.length;
    let preSum = new Array(n).fill(0);
    preSum[0] = nums[0];
    for (let i = 1; i < n; i++) {
        preSum[i] = preSum[i - 1] + nums[i];
    }

    //console.log(preSum);

    let count = 0;
    for (let i = 0; i < n; i++) {
        for (let j = i; j < n; j++) {
            if (i == j && nums[i] < k) {
                count++;
            } else if (i == 0 && preSum[j] * (j + 1) < k) {
                count++;
            } else if ((preSum[j] - preSum[i - 1]) * (j - i + 1) < k) {
                count++;
            } else {
                break;
            }
        }
    }
    return count;
};

//改成二分
var countSubarrays = function (nums, k) {
    let n = nums.length;
    let preSum = new Array(n).fill(0);
    preSum[0] = nums[0];
    for (let i = 1; i < n; i++) {
        preSum[i] = preSum[i - 1] + nums[i];
    }

    console.log(preSum);

    let count = 0;
    for (let i = 0; i < n; i++) {
        let left = i, right = n - 1 , middle = 0;
        while (left < right) {
            middle = left + Math.floor((right - left) / 2);
            let value = preSum[middle] - preSum[i] + nums[i];
            if (value * (middle - i + 1) >= k) {
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }

        let value = preSum[left] - preSum[i] + nums[i];
        if (value * (left - i + 1) >= k) {
            left--;
        }
        count += left - i + 1;
        
        //console.log(`${left} ${count}`);

    }
    return count;
};


// nums = [2, 1, 4, 3, 5], k = 10
nums = [1,1,1], k = 5

nums = [6,8,9,7], k = 50
nums = [5,2,6,8,9,7], k = 50
console.log(nums);
console.log(countSubarrays2(nums, k));
console.log(countSubarrays(nums, k));

