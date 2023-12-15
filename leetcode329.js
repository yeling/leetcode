/*
* auther yeling
* 329. 矩阵中的最长递增路径
* 回朔
*/

//135 / 138 个通过测试用例
var longestIncreasingPath2 = function (matrix) {
    let m = matrix.length;
    let n = matrix[0].length;
    let used = new Array(m);
    for (let i = 0; i < m; i++) {
        used[i] = new Array(n);
        used[i].fill(false);
    }
    let maxLen = 0;
    let dfsCount = 0;
    let dfs = function (matrix, m, n, i, j, used, preLen) {
        dfsCount++;
        if (i == -1 || i == m || j == -1 || j == n) {
            return;
        }
        //console.log(`${i} ${j} ${used} ${preLen}`)
        maxLen = Math.max(maxLen, preLen);
        if (i - 1 >= 0 && used[i - 1][j] == false && matrix[i - 1][j] > matrix[i][j]) {
            used[i - 1][j] = true;
            dfs(matrix, m, n, i - 1, j, used, preLen + 1);
            used[i - 1][j] = false;
        }
        if (i + 1 <= m - 1 && used[i + 1][j] == false && matrix[i + 1][j] > matrix[i][j]) {
            used[i + 1][j] = true;
            dfs(matrix, m, n, i + 1, j, used, preLen + 1);
            used[i + 1][j] = false;
        }
        if (j - 1 >= 0 && used[i][j - 1] == false && matrix[i][j - 1] > matrix[i][j]) {
            used[i][j - 1] = true;
            dfs(matrix, m, n, i, j - 1, used, preLen + 1);
            used[i][j - 1] = false;
        }
        if (j + 1 <= n - 1 && used[i][j + 1] == false && matrix[i][j + 1] > matrix[i][j]) {
            used[i][j + 1] = true;
            dfs(matrix, m, n, i, j + 1, used, preLen + 1);
            used[i][j + 1] = false;
        }
    }
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            dfs(matrix, m, n, i, j, used, 1);
        }
    }
    console.log(`dfsCount ${dfsCount}`)
    return maxLen;
};

//135 / 138 个通过测试用例
var longestIncreasingPath3 = function (matrix) {
    let m = matrix.length;
    let n = matrix[0].length;
    let used = new Array(m);
    let count = new Array(m);
    for (let i = 0; i < m; i++) {
        used[i] = new Array(n);
        used[i].fill(false);

        count[i] = new Array(n);
        count[i].fill(1);
    }
    let maxLen = 0;
    let currLen = 0;
    let dfsCount = 0;
    let dfs = function (matrix, m, n, i, j, used, preLen) {
        dfsCount++;
        if (i == -1 || i == m || j == -1 || j == n) {
            return;
        }
        //console.log(`${i} ${j} ${used} ${preLen}`)
        maxLen = Math.max(maxLen, preLen);
        currLen = Math.max(currLen, preLen);
        if (i - 1 >= 0 && used[i - 1][j] == false && matrix[i - 1][j] > matrix[i][j]) {
            if (count[i - 1][j] > 1) {
                maxLen = Math.max(maxLen, preLen + count[i - 1][j]);
                currLen = Math.max(currLen, preLen + count[i - 1][j]);
            } else {
                used[i - 1][j] = true;
                dfs(matrix, m, n, i - 1, j, used, preLen + 1);
                used[i - 1][j] = false;
            }
        }
        if (i + 1 <= m - 1 && used[i + 1][j] == false && matrix[i + 1][j] > matrix[i][j]) {
            used[i + 1][j] = true;
            dfs(matrix, m, n, i + 1, j, used, preLen + 1);
            used[i + 1][j] = false;
        }
        if (j - 1 >= 0 && used[i][j - 1] == false && matrix[i][j - 1] > matrix[i][j]) {
            if (count[i][j - 1] > 1) {
                maxLen = Math.max(maxLen, preLen + count[i][j - 1]);
                currLen = Math.max(currLen, preLen + count[i][j - 1]);
            } else {
                used[i][j - 1] = true;
                dfs(matrix, m, n, i, j - 1, used, preLen + 1);
                used[i][j - 1] = false;
            }
        }
        if (j + 1 <= n - 1 && used[i][j + 1] == false && matrix[i][j + 1] > matrix[i][j]) {
            count[i][j + 1]++;
            used[i][j + 1] = true;
            dfs(matrix, m, n, i, j + 1, used, preLen + 1);
            used[i][j + 1] = false;
        }
    }
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            currLen = 0;
            dfs(matrix, m, n, i, j, used, 1);
            count[i][j] = currLen;
        }
    }
    console.log(`dfsCount ${dfsCount}`)
    return maxLen;
};

//使用记忆化搜索，可以降低搜索次数
var longestIncreasingPath4 = function (matrix) {
    let m = matrix.length;
    let n = matrix[0].length;
    let used = new Array(m);
    let count = new Array(m);
    for (let i = 0; i < m; i++) {
        used[i] = new Array(n);
        used[i].fill(false);

        count[i] = new Array(n);
        count[i].fill(1);
    }
    let maxLen = 0;
    let currPath = [];
    let dfsCount = 0;
    let dfs = function (matrix, m, n, i, j, used, path) {
        dfsCount++;
        if (i == -1 || i == m || j == -1 || j == n) {
            return;
        }
        console.log(`${dfsCount} ${i} ${j} ${count.join(' ')}`)
        maxLen = Math.max(maxLen, path.length);
        if (currPath.length < path.length) {
            currPath = path.slice();
        }
        //console.log(count.join(' '));
        if (i - 1 >= 0 && used[i - 1][j] == false && matrix[i - 1][j] > matrix[i][j]) {
            if (count[i - 1][j] > 1) {
                maxLen = Math.max(maxLen, path.length + count[i - 1][j]);
                //currLen = Math.max(currLen,path.length + count[i-1][j]);
            } else {
                used[i - 1][j] = true;
                path.push({ i: i - 1, j: j });
                dfs(matrix, m, n, i - 1, j, used, path);
                path.pop();
                used[i - 1][j] = false;
            }
        }
        if (i + 1 <= m - 1 && used[i + 1][j] == false && matrix[i + 1][j] > matrix[i][j]) {
            if (count[i + 1][j] > 1) {
                maxLen = Math.max(maxLen, path.length + count[i + 1][j]);
            } else {
                used[i + 1][j] = true;
                path.push({ i: i + 1, j: j });
                dfs(matrix, m, n, i + 1, j, used, path);
                path.pop();
                used[i + 1][j] = false;
            }
        }
        if (j - 1 >= 0 && used[i][j - 1] == false && matrix[i][j - 1] > matrix[i][j]) {
            if (count[i][j - 1] > 1) {
                maxLen = Math.max(maxLen, path.length + count[i][j - 1]);
                //currLen = Math.max(currLen,path.length + count[i][j - 1]);
            } else {
                used[i][j - 1] = true;
                path.push({ i: i, j: j - 1 });
                dfs(matrix, m, n, i, j - 1, used, path);
                path.pop();
                used[i][j - 1] = false;
            }
        }
        if (j + 1 <= n - 1 && used[i][j + 1] == false && matrix[i][j + 1] > matrix[i][j]) {
            if (count[i][j + 1] > 1) {
                maxLen = Math.max(maxLen, path.length + count[i][j + 1]);
            } else {
                used[i][j + 1] = true;
                path.push({ i: i, j: j + 1 });
                dfs(matrix, m, n, i, j + 1, used, path);
                path.pop();
                used[i][j + 1] = false;
            }
        }
    }
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            currPath = [];
            let path = new Array();
            path.push({ i, j });
            dfs(matrix, m, n, i, j, used, path);
            count[i][j] = currPath.length;
            for (let k = 0; k < currPath.length; k++) {
                count[currPath[k].i][currPath[k].j] = currPath.length - k;
            }
        }
    }
    console.log(`dfsCount ${dfsCount}`)
    return maxLen;
};

//动态规划问题求解，从最小的节点开始求
var longestIncreasingPath = function (matrix) {
    let m = matrix.length;
    let n = matrix[0].length;
    let dp = new Array(m);
    for (let i = 0; i < m; i++) {
        dp[i] = new Array(n);
        dp[i].fill(1);
    }
    let dots = new Array();
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            dots.push({ x: i, y: j, val: matrix[i][j] });
        }
    }
    dots.sort((a, b) => {
        return a.val - b.val;
    })
    let maxLen = 1;
    let hasPath = true;
    // dots.forEach((item) => {
    //     console.log(item)
    // })
    //最长升序路径，有向图，最长路径问题
    for (let i = 0; i < dots.length && hasPath; i++) {
        let x = dots[i].x;
        let y = dots[i].y;
        if (x - 1 >= 0 && matrix[x][y] > matrix[x - 1][y]) {
            dp[x][y] = Math.max(dp[x][y], dp[x - 1][y] + 1);
        }
        if (x + 1 <= m - 1 && matrix[x][y] > matrix[x + 1][y]) {
            dp[x][y] = Math.max(dp[x][y], dp[x + 1][y] + 1);
        }
        if (y - 1 >= 0 && matrix[x][y] > matrix[x][y - 1]) {
            dp[x][y] = Math.max(dp[x][y], dp[x][y - 1] + 1);
        }
        if (y + 1 <= n - 1 && matrix[x][y] > matrix[x][y + 1]) {
            dp[x][y] = Math.max(dp[x][y], dp[x][y + 1] + 1);
        }
        maxLen = Math.max(maxLen, dp[x][y]);

        //console.log(dp.join(' '));
    }
    return maxLen;
    //最长升序路径，有向图，最长路径问题
}

let matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]];
matrix = [[7, 6, 1, 1], [2, 7, 6, 0], [1, 3, 5, 1], [6, 6, 3, 2]]
matrix = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]

// console.log('right ' + longestIncreasingPath3(matrix));
console.log('' + longestIncreasingPath(matrix));

