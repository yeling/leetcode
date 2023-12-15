/*
* auther yeling
* 
* 
*/
var isPossibleToCutPath = function (grid) {
    let row = grid.length;
    let col = grid[0].length;
    let n = row * col;
    let res = [];
    let dfn = new Array(n).fill(-1);
    let low = new Array(n).fill(n);
    let num = 0;

    connections = []
    for(let i = 0; i < row; i++) {
        for(let j = 0; j < col; j++) {
            if(grid[i][j] == 1) {
                if(i + 1 < row && grid[i + 1][j] == 1) {
                    connections.push([i*row + j, (i+1)*row + j])
                }
                if(j + 1 < col && grid[i][j + 1] == 1) {
                    connections.push([i*row + j, i*row + j + 1])
                }
            }
        }
    }


    let dfs = (allPos, index, father) => {
        // console.log(`dfs ${index}`);
        if (dfn[index] == -1) {
            dfn[index] = num++;
            low[index] = dfn[index];
        }
        let childs = allPos[index];
        for (let i = 0; i < childs.length; i++) {
            if (low[childs[i]] == n) {
                dfs(allPos, childs[i], index);
                low[index] = Math.min(low[index], low[childs[i]]);
            } else if (childs[i] != father) {
                low[index] = Math.min(low[index], low[childs[i]]);
            }
        }
        // console.log(dfn);
        // console.log(low);
        return low[index]

    }
    let allPos = new Array(n).fill(0).map(() => []);
    for (let i = 0; i < connections.length; i++) {
        allPos[connections[i][0]].push(connections[i][1]);
        allPos[connections[i][1]].push(connections[i][0]);
    }
    // console.log(allPos);
    dfs(allPos, 0, -1);
    // console.log(dfn);
    // console.log(low);

    for (let i = 0; i < connections.length; i++) {
        let curr = connections[i];
        if (dfn[curr[0]] < low[curr[1]] || dfn[curr[1]] < low[curr[0]]) {
            res.push(curr);
        }
    }
    
    console.log(res);

};

// grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
grid = [[1,1,1],[1,0,0],[1,1,1]]
console.log(isPossibleToCutPath(grid))

