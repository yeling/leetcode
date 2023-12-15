/*
* auther yeling
* 329. 矩阵中的最长递增路径
* 回朔
*/

var longestIncreasingPath = function(matrix) {
    let m = matrix.length;
    let n = matrix[0].length;
    let used = new Array(m);
    for(let i = 0; i < m; i++) {
        used[i] = new Array(n);
        used[i].fill(false);
    }
    let maxLen = 0;
    let dfs = function(matrix,m,n,i,j,used,preLen) {
        if(i == -1 || i == m || j == -1 || j == n) {
            return;
        }
        console.log(`${i} ${j} ${used} ${preLen}`)
        maxLen = Math.max(maxLen,preLen);
        if(i - 1 >= 0 && used[i-1][j] == false) {
            used[i-1][j] = true;
            dfs(matrix,m,n,i-1,j,used,preLen + 1);
            used[i-1][j] = false;
        }
        if(i + 1 <= m - 1 && used[i+1][j] == false) {
            used[i+1][j] = true;
            dfs(matrix,m,n,i+1,j,used,preLen + 1);
            used[i+1][j] = false;
        }
        if(j - 1 >= 0 && used[i][j-1] == false) {
            used[i][j-1] = true;
            dfs(matrix,m,n,i,j-1,used,preLen + 1);
            used[i][j-1] = false;
        }
        if(j + 1 <= n - 1 && used[i][j+1] == false) {
            used[i][j+1] = true;
            dfs(matrix,m,n,i,j+1,used,preLen + 1);
            used[i][j+1] = false;
        }
    }
    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            dfs(matrix,m,n,i,j,used,1);
        }
    }
    return maxLen;
};



let matrix = [[9,9,4],[6,6,8],[2,1,1]];
console.log(longestIncreasingPath(matrix));
