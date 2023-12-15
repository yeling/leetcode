/*
* auther yeling
* 
* 6193. 沙漏的最大总和
*/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxSum = function(grid) {
    //二维矩阵前缀和
    let m = grid.length;
    let n = grid[0].length;
    let preSum = new Array(m + 1).fill(0).map(() => new Array(n + 1).fill(0));
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            let sum = 0;
            for (let a = 0; a <= i; a++) {
                for (let b = 0; b <= j; b++) {
                    sum += grid[a][b];
                }
            }
            preSum[i + 1][j + 1] = sum;
        }
    }
    //console.log(preSum.join(' '));
    let max = 0;
    for (let i = 0; i + 2 <= m - 1; i++) {
        for (let j = 0; j + 2 <= n - 1; j++) {
            let curr = preSum[i+2+1][j+2+1] - preSum[i][j+2+1] -  preSum[i + 2 + 1][j] + preSum[i][j];
            curr = curr - grid[i+1][j] - grid[i+1][j+2];
            max = Math.max(max,curr);
            //console.log(`i=${i} j=${j} curr=${curr} max=${max}`);
        }
    }
    return max;
};

grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]];
// grid = [[1,2,3],[4,5,6],[7,8,9]];
console.log(maxSum(grid));