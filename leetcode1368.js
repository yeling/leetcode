/*
* auther yeling
* 1368. 使网格图至少有一条有效路径的最小代价
* 
*/

const {
PriorityQueue,
MinPriorityQueue,
MaxPriorityQueue,
} = require('@datastructures-js/priority-queue');

/**
 * @param {number[][]} grid
 * @return {number}
 */

var minCost = function (grid) {
    //Dijkstra 算法，贪心的一种
    //4个方向理解为4条边，边上权重为0，1，已经有方向了为0，否则代价为1
    //0,0 => m-1, n-1的最短路径
    let m = grid.length;
    let n = grid[0].length;
    let dis = new Array(m).fill(0).map(() => new Array(n).fill(Number.MAX_SAFE_INTEGER));
    let vis = new Array(m).fill(0).map(() => new Array(n).fill(false));
    dis[0][0] = 0;    
    let stack = new MinPriorityQueue({priority : (item) => item[2]});
    stack.enqueue([0,0,0]);
    let dirs = [[0,1],[0,-1],[1,0],[-1,0]];
    while(stack.isEmpty() == false) {
        //每次取出距离最近的进行遍历bfs
        let curr = stack.dequeue().element;
        vis[curr[0]][curr[1]] = true;
        for(let i = 0; i < dirs.length; i++) {
            let y = curr[0] + dirs[i][0];
            let x = curr[1] + dirs[i][1];
            //改点没有遍历过
            if(x >=0 && x < n && y >= 0 && y < m && vis[y][x] == false) {
                if(grid[curr[0]][curr[1]] == i + 1) {
                    dis[y][x] = Math.min(dis[y][x],dis[curr[0]][curr[1]]);
                } else {
                    dis[y][x] = Math.min(dis[y][x],dis[curr[0]][curr[1]] + 1);
                }
                stack.enqueue([y,x,dis[y][x]]);
            } 
        }
    }
    return dis[m-1][n-1];
}

grid = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]];
// grid = [[1,1,3],[3,2,2],[1,1,4]];

console.log(minCost(grid));

