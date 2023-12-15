/*
* auther yeling
* 
* 
*/

/**
 * @param {number[][]} grid
 * @return {number[][]}
 */
var largestLocal = function(grid) {
    let n = grid.length;
    let res = new Array(n-2).fill(0).map(() => new Array(n-2).fill(0));
    //console.log(res);
    for(let i = 1; i < n - 1; i++) {
        for(let j = 1; j < n -1; j++) {
            let max = grid[i][j];
            for(let ik = i - 1; ik <= i + 1; ik++) {
                for(let jk = j - 1; jk <= j + 1; jk++) {
                    max = Math.max(max,grid[ik][jk]);
                }
            }
            res[i-1][j-1] = max;
        }
    }
    return res;
};

grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
console.log('' + largestLocal(grid));