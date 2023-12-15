/*
* auther yeling
* 1799. N 次操作后的最大分数和
* 
*/

const {
    PriorityQueue,
    MinPriorityQueue,
    MaxPriorityQueue,
  } = require('@datastructures-js/priority-queue');

/**
 * @param {number[]} nums
 * @return {number}
 */
// 71 / 76
var maxScore2 = function(nums) {
    var gcd = function (a, b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    let n = nums.length;
    let dp = new Array(n).fill(0).map(() => new Array(n).fill(0));
    let stack = new MaxPriorityQueue((item) => item[2]);
    for(let i = 0; i < n; i++) {
        for(let j = i + 1; j < n; j++) {
            dp[i][j] = dp[j][i] = gcd(nums[i],nums[j]);
            // stack.enqueue([i,j,dp[i][j]]);
            stack.push([i,j,dp[i][j]],dp[i][j])
        }
    }
    //console.log(dp.join('\n'));
    let res = [];
    while(stack.isEmpty() == false) {
        let curr = stack.dequeue();
        //console.log(curr);
        res.push(curr[2]);
        let len = stack.size();
        let nextStack = new MaxPriorityQueue((item) => item[2]);
        for(let i = len - 1; i >= 0; i--) {
            let temp = stack.dequeue();
            if(temp[0] != curr[0] && temp[1] != curr[1]
                && temp[0] != curr[1] && temp[1] != curr[0]) {
                    nextStack.enqueue(temp);
                }
        }
        stack = nextStack;
    }
    console.log(res);
    let sum = 0;
    for(let i = n/2; i >= 1; i--) {
        sum += (n/2 - i + 1) * res[i-1];
    }
    return sum;
};

//42 / 75 个通过测试用例 TLE
//45 / 75 个通过测试用例 DFS + Cache
//56 / 75 个通过测试用例
//62 / 75 个通过测试用例

var maxScore = function(nums) {
    var gcd = function (a, b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    let n = nums.length;
    let dp = new Array(n).fill(0).map(() => new Array(n).fill(0));
    for(let i = 0; i < n; i++) {
        for(let j = i + 1; j < n; j++) {
            dp[i][j] = dp[j][i] = gcd(nums[i],nums[j]);
        }
    }

    let sum = 0;

    let cache = new Map();
    let dfs = (used, preSum, depth) => {
        //console.log(`dfs ${used} ${preSum} ${depth}`);
        let key = used.join('');
        let save = cache.get(key);
        if(save != null && save >= preSum) {
            //console.log('cache');
            return;
        }
        // console.log(key);
        cache.set(key, preSum);

        sum = Math.max(sum, preSum);
        for(let i = 0; i < n; i++) {
            for(let j = i+1; j < n; j++) {
                if(i != j && used[i] == 0 && used[j] == 0) {
                    used[i] = 1;
                    used[j] = 1;
                    dfs(used, preSum + depth * dp[i][j], depth + 1);
                    used[i] = 0;
                    used[j] = 0;
                }
            }
        }
    }
    let used = new Array(n).fill(0);
    dfs(used, 0, 1);
    return sum;
};

nums = [3,4,6,8]
nums = [1,2,3,4,5,6]
// nums = [1,2]
// nums = [415,705,471,230,902,87]

nums = [872673,231316,661413,836566,728814,541694,472746,234038,549345,680009]
// nums = [415,705,471,230,902,87,471,230,902,87,471,230,471,230]
// nums = [1373,1811,509,2503,113,421,79,1373,1811,509,2503,113,421,79]
// nums = [2069,2663,1087,2423,547,1871,1327,2069,2663,1087,2423,547,1871,1327]
 
label = 'maxScore'
console.time(label);
console.log(nums.length);
console.log(maxScore2(nums));
console.timeLog(label, 'maxScore2');
console.log(maxScore(nums));
console.timeEnd(label);
