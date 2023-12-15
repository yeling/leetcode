/*
* auther yeling
* 518. 零钱兑换 II
* 动态规划，dp问题
*/

/**
 * @param {number} amount
 * @param {number[]} coins
 * @return {number}
 */
var change = function(amount, coins) {
    let dp = new Array(amount + 1);
    dp.fill(0);
    dp[0] = 1;
    for(let i = 0; i < coins.length; i++) {
        for(let j = coins[i]; j <= amount; j++) {
            dp[j] = dp[j] + dp[j - coins[i]];
        }
    }
    return dp[amount];
};


let amount = 5, coins = [1, 2, 5];
console.log(change(5,coins));

