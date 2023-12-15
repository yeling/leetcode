/*
* auther yeling
* 1219. 黄金矿工
* 
*/
/**
 * @param {number[][]} grid
 * @return {number}
 */
var getMaximumGold = function (matrix) {
    let m = matrix.length;
    let n = matrix[0].length;
    let used = new Array(m);
    for (let i = 0; i < m; i++) {
        used[i] = new Array(n);
        used[i].fill(false);
    }
    let maxLen = 0;
    let dfs = function (matrix, m, n, i, j, used, preLen) {
        if (i == -1 || i == m || j == -1 || j == n) {
            return;
        }
        //console.log(`${i} ${j} ${used} ${preLen}`)
        maxLen = Math.max(maxLen, preLen);
        if (i - 1 >= 0 && used[i - 1][j] == false && matrix[i - 1][j] != 0) {
            used[i][j] = true;
            dfs(matrix, m, n, i - 1, j, used, preLen + matrix[i - 1][j]);
            used[i][j] = false;
        }
        if (i + 1 <= m - 1 && used[i + 1][j] == false && matrix[i + 1][j] != 0) {
            used[i][j] = true;
            dfs(matrix, m, n, i + 1, j, used, preLen + matrix[i + 1][j]);
            used[i][j] = false;
        }
        if (j - 1 >= 0 && used[i][j - 1] == false && matrix[i][j - 1] != 0) {
            used[i][j] = true;
            dfs(matrix, m, n, i, j - 1, used, preLen + matrix[i][j - 1]);
            used[i][j] = false;
        }
        if (j + 1 <= n - 1 && used[i][j + 1] == false && matrix[i][j + 1] != 0) {
            used[i][j] = true;
            dfs(matrix, m, n, i, j + 1, used, preLen + matrix[i][j + 1]);
            used[i][j] = false;
        }
    }
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if(matrix[i][j] != 0) {
                dfs(matrix, m, n, i, j, used, matrix[i][j]);
            }   
        }
    }
    return maxLen;
};

grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
// grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5]]
// grid = [[1, 0, 7], [2, 0, 6]];
console.log(getMaximumGold(grid))


