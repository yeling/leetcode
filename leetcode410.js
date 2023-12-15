/*
* auther yeling
* 410. 分割数组的最大值
* 
*/

/**
 * @param {number[]} nums
 * @param {number} m
 * @return {number}
 */
var splitArray = function (nums, m) {
    let n = nums.length;
    let preSum = new Array(n + 1).fill(0);
    let dp = new Array(n).fill(0).map((value) => { return new Array(m).fill(Number.MAX_VALUE) });
    nums.forEach((item, index) => {
        if (index > 0) {
            preSum[index] = preSum[index - 1] + item;
        } else {
            preSum[index] = item;
        }
    })
    preSum[n] = preSum[n -1]; 
    //console.log(preSum);
    //console.log(dp);
    for(let j = 0; j < m; j++) {
        for(let i = j; i < n; i++) {
            if(j == 0) {
                dp[i][j] = preSum[i];
            } else {
                for(let k = j - 1; k < i; k++) {
                    dp[i][j] = Math.min(dp[i][j],Math.max(dp[k][j-1],preSum[i] - preSum[k]));
                }
            }
        }
    }
    //console.log(dp.join('\n'));
    return dp[n-1][m-1];

};

nums = [7, 2, 5, 10, 8], m = 2
nums = [2,4,4,2], m = 2
console.log(`${splitArray(nums, m)}`);