/*
* auther yeling
* 2267. 检查是否有合法括号字符串路径
* 
*/

/**
 * @param {character[][]} grid
 * @return {boolean}
 */
var hasValidPath = function(grid) {
    
    let m = grid.length;
    let n = grid[0].length;
    if(grid[0][0] == ')' || grid[m - 1][n - 1] == '(') {
        return false;
    }
    let dp = new Array(m).fill(0).map(() => new Array(n).fill(0).map(() => new Set()));
    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            if(j > 0) {
                dp[i][j - 1].forEach((item) => {
                    let curr = item;
                    if(grid[i][j] == '(') {
                        curr++;
                    } else if(grid[i][j] == ')') {
                        curr--;
                    }
                    if(curr >= 0) {
                        dp[i][j].add(curr)
                    }
                });
            } 
            if(i > 0) {
                dp[i - 1][j].forEach((item) => {
                    let curr = item;
                    if(grid[i][j] == '(') {
                        curr++;
                    } else if(grid[i][j] == ')') {
                        curr--;
                    }
                    if(curr >= 0) {
                        dp[i][j].add(curr)
                    }
                });
            }
            
            if(j == 0 && i == 0) {
                if(grid[i][j] == '(') {
                    dp[i][j].add(1);
                }
            }
            // console.log(`${i} ${j}`);
            // console.log(dp[i][j]);
        }
    }

    if(dp[m - 1][n - 1].has(0)) {
        return true;
    } else {
        return false;
    }

};


grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
console.log(hasValidPath(grid));
