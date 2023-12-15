/*
* auther yeling
* 629. K个逆序对数组
* 
*/

/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */

let MOD = 10 ** 9 + 7;
var kInversePairs = function(n, k) {
    let dp = new Array(n + 1).fill(0).map(() => new Array(k + 1).fill(0));    
    for(let i = 1; i <= n; i++) {        
        for(let j = 0; j <= k; j++) {            
            if(j == 0) {
                dp[i][j] = 1;
            } else {
                let ti = Math.min(k, i-1);
                for(; ti >= 0; ti--) {
                    if( j - ti >= 0) {
                        dp[i][j] = (dp[i][j] +  dp[i - 1][j - ti])%MOD;
                    }                    
                }
            }
        }
    }
    console.log(dp.join('\n'));
    return dp[n][k];
};


n = 3, k = 2;
// n = 4, k = 5;
n = 10, k = 2;
console.log(kInversePairs(n,k));
