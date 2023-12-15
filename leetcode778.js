/*
* auther yeling
* 778. 水位上升的泳池中游泳
* 并查集，水位上升后，将0，0的节点连通
*/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var swimInWater = function (grid) {
    let m = grid.length;
    let n = grid[0].length;
    let father = new Array(m);
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            father[i * m + j] = i * m + j;
        }
    }
    let height = Math.max(grid[0][0], grid[m - 1][n - 1]);
    while (true) {
        console.log(`${height}`)
        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n; j++) {
                if (grid[i][j] - height <= 0) {
                    if (i - 1 >= 0 && grid[i - 1][j] - height <= 0) {
                        join(father, i * n + j, (i - 1) * n + j);
                    }
                    if (i + 1 <= m - 1 && grid[i + 1][j] - height <= 0) {
                        join(father, i * n + j, (i + 1) * n + j);
                    }
                    if (j - 1 >= 0 && grid[i][j - 1] - height <= 0) {
                        join(father, i * n + j, i * n + j - 1);
                    }
                    if (j + 1 <= n - 1 && grid[i][j + 1] - height <= 0) {
                        join(father, i * n + j, i * n + j + 1);
                    }
                }

            }
        }
        let fu = find(father, 0);
        let fv = find(father, m*n - 1);
        if(fu == fv) {
            break;
        } else {
            height++;
        }
    }
    return height;
};

//查找father
var find = function (father, u) {
    if (father[u] != u) {
        father[u] = find(father, father[u])
    }
    return father[u];
}

//合并
var join = function (father, u, v) {
    let fu = find(father, u);
    let fv = find(father, v);
    if (fu != fv) {
        father[fu] = fv;
    }
}

let grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
console.log(swimInWater(grid));
