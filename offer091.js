/*
* auther yeling
*剑指 Offer II 091. 粉刷房子
*/
/**
 * @param {number[][]} costs
 * @return {number}
 */
var minCost = function(costs) {
    let n = costs.length;
    let dp = new Array(n);
    dp[0] = new Array(3);
    dp[0] = costs[0].slice();
    for(let i = 1; i < n; i++) {
        dp[i] = new Array(3);
        dp[i][0] = costs[i][0] + Math.min(dp[i - 1][1], dp[i-1][2]);
        dp[i][1] = costs[i][1] + Math.min(dp[i - 1][0], dp[i-1][2]);
        dp[i][2] = costs[i][2] + Math.min(dp[i - 1][1], dp[i-1][0]);
    }
    return Math.min(dp[n-1][0],dp[n-1][1],dp[n-1][2]);
};

let costs = [[17,2,17],[16,16,5],[14,3,19]];

console.log(minCost(costs));