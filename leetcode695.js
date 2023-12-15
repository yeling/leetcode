/*
* auther yeling
* 695. 岛屿的最大面积
* 并查集求出岛屿数量
*/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function(grid) {
    let m = grid.length;
    let n = grid[0].length;
    let father = new Array(m*n);
    for(let i = 0; i < father.length; i++) {
        father[i] = i;
    }
    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            if(grid[i][j] == 1) {
                //上
                if(i - 1 >= 0 && grid[i-1][j] == 1) {
                    join(father,i*n + j, (i-1)*n + j);
                }
                //下
                if(i + 1 < m && grid[i+1][j] == 1) {
                    join(father,i*n + j, (i+1)*n + j);
                }
                //左
                if(j - 1 >= 0 && grid[i][j-1] == 1) {
                    join(father,i*n + j, i*n + j - 1);
                }
                //右
                if(i + 1 < n && grid[i][j+1] == 1) {
                    join(father,i*n + j, i*n + j + 1);
                }
            }
        }
    }
    //console.log(father);
    let isMap = new Map();
    for(let i = 0; i < father.length; i++) {
        let root = find(father,father[i])
        if(grid[Math.floor(root/n)][root%n] == 1) {
            let num = isMap.get(root);
            if(num == null) {
                num = 0;
            }
            num++;
            isMap.set(root,num);
        }
    }
    //console.log(isMap);
    let maxSum = 0;
    isMap.forEach((value,key) => {
        //console.log(`key ${key} value ${value}`);
        maxSum = Math.max(maxSum,value);
    })
    
    return maxSum;
};

//查找father
var find = function(father, u) {
    //可以将少节点数目
    if(father[u] != u) {
        father[u] = find(father,father[u])
    }
    return father[u];
}

//合并
var join = function(father, u, v) {
    let fu = find(father,u);
    let fv = find(father,v);
    if(fu != fv) {
        father[fu] = fv;
    }
}

let grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]];
//grid = [[0,0,1,1,1,0,0,1,0,0,0,0,0]];
console.log(maxAreaOfIsland(grid));