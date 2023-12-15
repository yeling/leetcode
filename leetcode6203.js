/*
* auther yeling
* 
* 
*/

/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number}
 */
var numberOfPaths = function(grid, k) {
    let MOD = 10 ** 9 + 7;
    let m = grid.length;
    let n = grid[0].length;
    let dp = new Array(m).fill(0).map(() => new Array(n).fill(0).map(() => new Array(k).fill(0)));
    if(k == 1) {
        for(let i = 0; i < m; i++) {
            for(let j = 0; j < n; j++) {
                if(i == 0 || j == 0) {
                    dp[i][j][0] = 1;
                } else {
                    dp[i][j][0] = (dp[i - 1][j][0] + dp[i][j - 1][0])%MOD;
                }
            }
        }
        return dp[m-1][n-1][0]%MOD;
    }

    dp[0][0][grid[0][0]%k] = 1;
    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            if(i == 0) {
                if(j > 0) {
                    for(let ki = 0; ki < k; ki++) {                        
                        dp[i][j][(ki + grid[i][j])%k] = dp[i][j-1][ki]%MOD;
                    }
                }
            } else if(j == 0) {
                if(i > 0) {
                    for(let ki = 0; ki < k; ki++) {                        
                        dp[i][j][(ki + grid[i][j])%k] = dp[i - 1][j][ki]%MOD;
                    }
                }
            } else {
                for(let ki = 0; ki < k; ki++) {                        
                    dp[i][j][(ki + grid[i][j])%k] += dp[i - 1][j][ki]%MOD;
                    dp[i][j][(ki + grid[i][j])%k] += dp[i][j-1][ki]%MOD;
                }
            }
        }
    }
    return dp[m-1][n-1][0]%MOD;



    

};

grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
// grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0],[2,3,7,0]], k = 1
console.log(numberOfPaths(grid,k))