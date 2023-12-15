/*
* auther yeling
* 2050. 并行课程 III
* 
*/

/**
 * @param {number} n
 * @param {number[][]} relations
 * @param {number[]} time
 * @return {number}
 */
var minimumTime = function (n, relations, time) {
    //拓扑排序，计算出度，入度，当前时间为入度的max，拓扑排序+动态规划
    let inDegree = new Array(n + 1).fill(0);
    let outList = new Array(n + 1).fill(0).map(() => new Set());
    let maxTime = new Array(n + 1).fill(0);
    for (let i = 0; i < relations.length; i++) {
        let edge = relations[i];
        if (outList[edge[0]].has(edge[1]) == false) {
            outList[edge[0]].add(edge[1]);
            inDegree[edge[1]]++;
        }
    }

    let res = 0;
    let stack = new Array();
    for (let i = 1; i <= n; i++) {
        if (inDegree[i] == 0) {
            stack.push(i);
            maxTime[i] = time[i - 1];
            res = Math.max(res, maxTime[i]);
        }
    }

    while (stack.length > 0) {
        //所有入度为0的，对应的出度列表，入度值减1
        for (let i = 0; i < stack.length; i++) {
            let currOut = outList[stack[i]];
            currOut.forEach((value) => {
                inDegree[value]--;
                maxTime[value] = Math.max(maxTime[value], maxTime[stack[i]] + time[value - 1]);
                res = Math.max(res, maxTime[value]);
            })
            inDegree[stack[i]] = -1;
        }

        //重新计算入度数组
        stack.length = 0;
        for (let i = 1; i <= n; i++) {
            if (inDegree[i] == 0) {
                stack.push(i);
            }
        }
    }
    return res;

};

n = 3, relations = [[1,3],[2,3]], time = [3,2,5]
// n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]
// n = 2
// relations = [[2,1]]
// time = [10000,10000]
console.log(minimumTime(n, relations, time));