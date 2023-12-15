/*
* auther yeling
* 1260. 二维网格迁移
* 
*/

/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 */
var shiftGrid = function(grid, k) {
    let m = grid.length;
    let n = grid[0].length;
    k = k%(m*n);
    let cache = [];
    for(let i = m*n - k; i < m*n ; i++) {
        cache.push(grid[Math.floor(i/n)][i%n]);
    } 
    for(let i = m*n - 1; i >= k; i--) {
        grid[Math.floor(i/n)][i%n] = grid[Math.floor((i-k)/n)][(i-k)%n];
    }
    for(let i = 0; i < k; i++) {
        grid[Math.floor(i/n)][i%n] = cache[i];
    }
    // console.log(cache);
    // console.log(grid.join('\n'));
    return grid;
};

grid = [[1,2,3],[4,5,6],[7,8,9]], k = 11;
console.log(grid.join('\n'));

console.log(`${shiftGrid(grid,k)}`);
