/*
* auther yeling
* 200. 岛屿数量
*/
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    let used = [];
    let m = grid.length;
    let n = grid[0].length
    for(let i = 0; i < m; i++) {
        used.push(new Array(n));
        used[i].fill(false);
    }
    let sum = 0;
    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            if(grid[i][j] == 1 && used[i][j] == false) {
                sum++;
                dfs(grid, m, n, i, j,used);
            }
        }
    }
    return sum;
};

var dfs = function(grid, m, n, i, j, used) {
    if(i == m || i == -1 || j == n || j == -1) {
        return;
    }
    //console.log(`dfs ${i} ${j} grid ${grid[i][j]} used ${used[i][j]}`)
    if(grid[i][j] == 0) {
        return;
    }
    if(grid[i][j] == 1 && used[i][j] == true) {
        return;
    }
     //四个方向的dfs
    used[i][j] = true;
    dfs(grid,m,n,i-1,j,used);
    dfs(grid,m,n,i+1,j,used);
    dfs(grid,m,n,i,j+1,used);
    dfs(grid,m,n,i,j-1,used);
}

let grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ];

// grid = [
//     ["1","1","0","0","0"],
//     ["1","1","0","0","0"],
//     ["0","0","1","0","0"],
//     ["0","0","0","1","1"]
// ];
  
console.log(numIslands(grid));

