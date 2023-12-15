/*
* auther yeling
* 1563. 石子游戏 V
* 
*/
/**
 * @param {number[]} stoneValue
 * @return {number}
 */
//76 / 132
var stoneGameV2 = function (stoneValue) {
    let n = stoneValue.length;
    if (n == 1) {
        return 0;
    }
    let preSum = new Array(n + 1).fill(0);
    //preSum[0] = stoneValue[0];
    for (let i = 0; i < n; i++) {
        preSum[i + 1] = preSum[i] + stoneValue[i];
    }
    let left = 0, right = n - 1;
    let sum = 0;
    while (left < right) {
        //console.log(`${left} ${right} ${sum}`);
        let min = Number.MAX_SAFE_INTEGER;
        let index = 0;
        for (let i = left + 1; i <= right; i++) {
            let curr = Math.abs(preSum[i] - preSum[left] - (preSum[right + 1] - preSum[i]));
            if (curr < min) {
                min = Math.abs(preSum[i] - preSum[left] - (preSum[right + 1] - preSum[i]));
                index = i;
            }
        }
        let diff = preSum[index] - preSum[left] - (preSum[right + 1] - preSum[index]);
        if (diff < 0) {
            sum += preSum[index] - preSum[left];
            right = index - 1;
        } else if (min == 0 && index - left > right - index) {
            sum += preSum[index] - preSum[left];
            right = index - 1;
        } else {
            sum += preSum[right + 1] - preSum[index];
            left = index;
        }
    }
    return sum;
};

var stoneGameV = function (stoneValue) {
    let n = stoneValue.length;
    if (n == 1) {
        return 0;
    }
    let preSum = new Array(n + 1).fill(0);
    //preSum[0] = stoneValue[0];
    for (let i = 0; i < n; i++) {
        preSum[i + 1] = preSum[i] + stoneValue[i];
    }
    let dp = new Array(n).fill(0).map(() => new Array(n).fill(-1));
    let dfs = (i, j) => {
        //console.log(`dsf ${i} ${j}`);
        if(dp[i][j] != -1) {
            return dp[i][j];
        }
        if (i == j) {
            dp[i][j] = 0;
            return dp[i][j];
        }
        let max = 0;
        for (let k = i; k < j; k++) {
            let diff = preSum[j + 1] - preSum[k + 1] - (preSum[k + 1] - preSum[i]);
            if (diff > 0) {
                max = Math.max(max, dfs(i, k) + preSum[k + 1] - preSum[i]);
            } else if (diff == 0) {
                max = Math.max(max, dfs(i, k) + preSum[k + 1] - preSum[i], dfs(k + 1, j) + preSum[j + 1] - preSum[k + 1]);
            } else {
                max = Math.max(max, dfs(k + 1, j) + preSum[j + 1] - preSum[k + 1]);
            }
        }
        dp[i][j] = max;
        return dp[i][j];
    }
    dfs(0, n-1);
    //console.log(dp.join('\n'));
    return dp[0][n-1];
};
stoneValue = [6, 2, 3, 4, 5, 5];
// stoneValue = [1, 1, 2];
// stoneValue = [1, 4, 2, 3];
// stoneValue = [1, 4];
label = 'stoneGameV';
console.time(label);
console.log(stoneGameV2(stoneValue));
console.timeLog(label, 'stoneGameV')
console.log(stoneGameV(stoneValue));
console.timeEnd(label);