/*
* auther yeling
* 
* 
*/

/**
 * @param {number} k
 * @param {number[][]} rowConditions
 * @param {number[][]} colConditions
 * @return {number[][]}
 */
var buildMatrix = function (k, rowConditions, colConditions) {
    let res = new Array(k).fill(0).map(() => new Array(k).fill(0));
    let n = rowConditions.length;
    let m = colConditions.length;

    let arrryStack = new Array();
    arrryStack.push([]);
    for (let i = 0; i < n; i++) {
        let posAbove = -1;
        let posBelow = -1;
        let curr = rowConditions[i];
        let len = arrryStack.length;
        for (let k = 0; k < len; k++) {
            let preArray = arrryStack[k];
            for (let j = 0; j < preArray.length; j++) {
                if (preArray[j] == curr[1]) {
                    posBelow = j;
                }
                if (preArray[j] == curr[0]) {
                    posAbove = j;
                }
            }

            if (posAbove > posBelow) {
                return [];
            }

            if (posBelow == -1 && posAbove != -1) {
                //无约束，posAbove 后面所有位置都可以插入

            } else if (posAbove == -1 && posBelow != -1) {
                //posBelow 前面所有位置都可以插入

            } else if (posBelow == -1 && posAbove == -1) {
                //posBelow 所有位置都可以插入，满足条件即可

            } else {
                //两个位置刚好满足条件，不处理
            }
        }
    }
};

var buildMatrix2 = function (k, rowConditions, colConditions) {

    let calcPath = (k, edges) => {
        let inDegree = new Array(k + 1).fill(0);
        let outList = new Array(k + 1).fill(0).map(() => new Set());
        for (let i = 0; i < edges.length; i++) {
            let edge = edges[i];
            if(outList[edge[0]].has(edge[1]) == false) {
                outList[edge[0]].add(edge[1]);
                inDegree[edge[1]]++;
            }
        }

        let stack = new Array();
        for (let i = 1; i <= k; i++) {
            if (inDegree[i] == 0) {
                stack.push(i);
            }
        }

        let rowPath = [];
        while (stack.length > 0) {
            //所有入度为0的，对应的出度列表，入度值减1
            for (let i = 0; i < stack.length; i++) {
                let currOut = outList[stack[i]];
                currOut.forEach((value) => {
                    inDegree[value]--;
                })
                inDegree[stack[i]] = -1;
                rowPath.push(stack[i]);
            }

            //重新计算入度数组
            stack.length = 0;
            for (let i = 1; i <= k; i++) {
                if (inDegree[i] == 0) {
                    stack.push(i);
                }
            }

        }
        //console.log(rowPath);
        return rowPath;
    }
    
    let rowPath = calcPath(k,rowConditions);
    //console.log(rowPath);
    if(rowPath.length < k) {
        return [];
    }

    let colPath = calcPath(k,colConditions);
    //console.log(colPath);
    if(colPath.length < k) {
        return [];
    }

    let res = new Array(k).fill(0).map(() => new Array(k).fill(0));
    let pos = new Array(k + 1).fill(0).map(() => [0,0]);
    for(let i = 0; i < k; i++) {
        pos[rowPath[i]][0] = i;
        pos[colPath[i]][1] = i;
    }
    //console.log(pos.join(' '));

    for(let i = 1; i <= k; i++) {
        res[pos[i][0]][pos[i][1]] = i;
    }
    //console.log(res);
    return res;

}

k = 3, rowConditions = [[1, 2], [3, 2], [1,2]], colConditions = [[2, 1], [3, 2]]
console.log(buildMatrix2(k, rowConditions, colConditions));
