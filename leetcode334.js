/*
* auther yeling
* 334. 递增的三元子序列
* 贪心算法，记录first second
*/

//时间复杂度 O(n^3)
var increasingTriplet = function (nums) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            for (let k = j + 1; k < nums.length; k++) {
                if (nums[i] < nums[j] && nums[j] < nums[k]) {
                    return true;
                }
            }
        }
    }
    return false;
};

//引入dp数组之后，时间复杂度为O(n^2)
//75 / 76 个通过测试用例
var increasingTriplet2 = function (nums) {
    let dp = new Array(nums.length);
    dp.fill(1);
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] < nums[j]) {
                dp[j] = Math.max(dp[j], dp[i] + 1);
                //console.log(`${dp}`);
                if (dp[j] == 3) {
                    return true;
                }
            }
            
        }
    }
    return false;
};

var increasingTriplet3 = function (nums) {
    let first = nums[0];
    let second = Number.MAX_VALUE;
    for (let i = 1; i < nums.length; i++) {
        if(nums[i] > second) {
            return true;
        } else if(nums[i] > first) {
            second = nums[i];
        } else {
            first = nums[i];
        }
        // console.log(`first ${first} second ${second}`)
    }
    return false;
};

let nums = [2, 1, 5, 0, 6];
// nums = [5,4,4,6];

console.log(`1 ${increasingTriplet(nums)}`);
console.log(`2 ${increasingTriplet2(nums)}`);
console.log(`2 ${increasingTriplet3(nums)}`);