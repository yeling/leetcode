/*
* auther yeling
* 
* 
*/

/**
 * @param {number} low
 * @param {number} high
 * @param {number} zero
 * @param {number} one
 * @return {number}
 */
var countGoodStrings = function(low, high, zero, one) {
    let mod = 10 ** 9 + 7
    let len = high + 1 + Math.max(zero, one)
    let dp = new Array(len).fill(0).map(() => new Array(2).fill(0))
    sum = 0;
    dp[one][1] = 1;
    dp[zero][0] = 1;
    for(let i = 1; i <= high; i++) {
        dp[i + zero][0] += (dp[i][0] + dp[i][1])%mod;
        dp[i + one][1] += (dp[i][0] + dp[i][1])%mod;
        if(i >= low) {
            sum += (dp[i][0] + dp[i][1])%mod;
        }
    }
    return sum%mod;
};

low = 2, high = 3, zero = 1, one = 2
low = 3, high = 3, zero = 1, one = 1
console.log(countGoodStrings(low, high, zero, one))
