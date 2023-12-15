/*
* auther yeling
* 6110. 网格图中递增路径的数目
* 定义direction数组
*/

let MOD = Math.pow(10, 9) + 7;
//入度概念，会丢失部分数据，拓扑排序
var countPaths = function (grid) {
    let m = grid.length;
    let n = grid[0].length;
    let matrix = new Array(m);
    let result = 0;
    for (let i = 0; i < m; i++) {
        matrix[i] = new Array(n);
        matrix[i].fill(0);
        result = (result + n) % MOD;
    }
    let stack = new Array();
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (j + 1 <= n - 1 && grid[i][j] < grid[i][j + 1]) {
                matrix[i][j]++;
            }
            if (j - 1 >= 0 && grid[i][j] < grid[i][j - 1]) {
                matrix[i][j]++;
            }
            if (i + 1 <= m - 1 && grid[i][j] < grid[i + 1][j]) {
                matrix[i][j]++;
            }
            if (i - 1 >= 0 && grid[i][j] < grid[i - 1][j]) {
                matrix[i][j]++;
            }
            if (matrix[i][j] == 0) {
                stack.push({ i, j });
            }
        }
    }
    while (stack.length > 0) {
        left = 0;
        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n; j++) {
                if (matrix[i][j] > 0) {
                    result = (result + matrix[i][j]) % MOD;
                }
            }
        }
        console.log(`${matrix.join(' ')}  ${stack.length} ${result}`)
        let len = stack.length;
        let k = 0;
        while (k < len) {
            k++
            let index = stack.shift();
            let i = index.i; let j = index.j;
            if (j + 1 <= n - 1 && grid[i][j] > grid[i][j + 1]) {
                matrix[i][j + 1]--;
                if (matrix[i][j + 1] == 0) {
                    stack.push({ i, j: j + 1 });
                }
            }
            if (j - 1 >= 0 && grid[i][j] > grid[i][j - 1]) {
                matrix[i][j - 1]--;
                if (matrix[i][j - 1] == 0) {
                    stack.push({ i, j: j - 1 });
                }
            }
            if (i + 1 <= m - 1 && grid[i][j] > grid[i + 1][j]) {
                matrix[i + 1][j]--;
                if (matrix[i + 1][j] == 0) {
                    stack.push({ i: i + 1, j });
                }
            }
            if (i - 1 >= 0 && grid[i][j] > grid[i - 1][j]) {
                matrix[i - 1][j]--;
                if (matrix[i - 1][j] == 0) {
                    stack.push({ i: i - 1, j });
                }
            }
        }
    }
    return result;
};

//先排序，从最小的节点开始计算，周围大于他的节点，数据累加
var countPaths2 = function (grid) {
    let m = grid.length;
    let n = grid[0].length;
    let dp = new Array(m);
    for (let i = 0; i < m; i++) {
        dp[i] = new Array(n);
        dp[i].fill(1);
    }
    let dots = new Array();
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            dots.push({ x: i, y: j, val: grid[i][j] });
        }
    }
    dots.sort((a, b) => {
        return a.val - b.val;
    })
    // dots.forEach((item) => {
    //     console.log(item)
    // })
    //最长升序路径，有向图，最长路径问题
    for (let i = 0; i < dots.length; i++) {
        let x = dots[i].x;
        let y = dots[i].y;
        if (x - 1 >= 0 && grid[x][y] < grid[x - 1][y]) {
            dp[x - 1][y] = (dp[x][y] + dp[x - 1][y]) % MOD;;
        }
        if (x + 1 <= m - 1 && grid[x][y] < grid[x + 1][y]) {
            dp[x + 1][y] = (dp[x][y] + dp[x + 1][y]) % MOD;;
        }
        if (y - 1 >= 0 && grid[x][y] < grid[x][y - 1]) {
            dp[x][y - 1] = (dp[x][y] + dp[x][y - 1]) % MOD;;
        }
        if (y + 1 <= n - 1 && grid[x][y] < grid[x][y + 1]) {
            dp[x][y + 1] = (dp[x][y] + dp[x][y + 1]) % MOD;;
        }
        // console.log(dots[i])
        // console.log(` ${dp.join(' ')}`);
    }
    let result = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            result = (result + dp[i][j]) % MOD;
        }
    }
    return result;
}

let matrix = [[1, 1], [3, 4]];
matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]];
// matrix = [[8,7,6]];
// 148
matrix = [[12469, 18741, 68716, 30594, 65029, 44019, 92944, 84784, 92781, 5655, 43120, 81333, 54113, 88220, 23446, 6129, 2904, 48677, 20506, 79604, 82841, 3938, 46511, 60870, 10825, 31759, 78612, 19776, 43160, 86915, 74498, 38366, 28228, 23687, 40729, 42613, 61154, 22726, 51028, 45603, 53586, 44657, 97573, 61067, 27187, 4619, 6135, 24668, 69634, 24564, 30255, 51939, 67573, 87012, 4106, 76312, 28737, 7704, 35798]];
// console.log(`${matrix.length} ${matrix[0].length}`)
console.log(countPaths2(matrix));