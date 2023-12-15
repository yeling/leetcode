/*
* auther yeling
* 
* 
*/

/**
 * @param {number} n
 * @param {number[][]} relations
 * @param {number} k
 * @return {number}
 */
//66 / 81
var minNumberOfSemesters2 = function(n, relations, k) {
    //拓扑排序，计算出度，入度，每次计算K个
    let inDegree = new Array(n + 1).fill(0);
    let outList = new Array(n + 1).fill(0).map(() => new Set());
    let sum = 0;
    for (let i = 0; i < relations.length; i++) {
        let edge = relations[i];
        if (outList[edge[0]].has(edge[1]) == false) {
            outList[edge[0]].add(edge[1]);
            inDegree[edge[1]]++;
        }
    }

    let stack = new Array();
    for (let i = 1; i <= n && stack.length <= k; i++) {
        if (inDegree[i] == 0) {
            stack.push(i);
        }
    }

    while (stack.length > 0) {
        //所有入度为0的，对应的出度列表，入度值减1
        console.log(stack);
        let len = stack.length;
        for (let i = 0; i < k && i < len; i++) {
            let index = stack.pop();
            // let index = stack.shift();
            let currOut = outList[index];
            currOut.forEach((value) => {
                inDegree[value]--;
            })
            inDegree[index] = -1;
        }
        sum++;

        //重新计算入度数组
        stack.length = 0;
        for (let i = 1; i <= n && stack.length <= k; i++) {
            if (inDegree[i] == 0) {
                stack.push(i);
            }
        }
    }
    return sum;

};

var minNumberOfSemesters = function(n, relations, k) {
    //dp
    //拓扑排序，计算出度，入度，每次计算K个
    let inDegree = new Array(n + 1).fill(0);
    let outList = new Array(n + 1).fill(0).map(() => new Set());
    
    for (let i = 0; i < relations.length; i++) {
        let edge = relations[i];
        if (outList[edge[0]].has(edge[1]) == false) {
            outList[edge[0]].add(edge[1]);
            inDegree[edge[1]]++;
        }
    }

    let stack = new Array();
    for (let i = 1; i <= n; i++) {
        if (inDegree[i] == 0) {
            stack.push(i);
        }
    }

    
    let dfs = (stack, inDegree, outList, used, index, path, preLen) => {
        console.log(`${stack} ${index} path ${path} plen ${path.length}`)
        // if(stack.length - index < k - path.length) {
        //     return n;
        // }
        stack = stack.map((value) => value);

        if(index == stack.length) {
            //重新计算入度数组
            stack.length = 0;
            let pathUsed = new Array(n + 1).fill(false);
            path.forEach((value) => {
                pathUsed[value] = true;
            })
            for (let i = 1; i <= n; i++) {
                if (inDegree[i] == 0 && used[i] == false) {
                    stack.push(i);
                }
            }
            //进入下一轮的标志
            if(stack.length == 0 && (path.length != k || preLen == n)) {
                let isEnd = true;
                for(let i = 1; i <= n; i++) {
                    //if(inDegree[i] >= 0 && used[i] == false) {
                    if(inDegree[i] >= 0) {
                        isEnd = false;
                        break;
                    }
                }
                return isEnd ? 1 : n;
            } else {
                let pathUsed = new Array(n + 1).fill(false);
                path.forEach((value) => {
                    pathUsed[value] = true;
                })
                stack.length = 0;
                for (let i = 1; i <= n; i++) {
                    if (inDegree[i] == 0 && pathUsed[i] == false) {
                        stack.push(i);
                        used[i] = false;
                    }
                }
                let sum = dfs(stack, inDegree, outList, used, 0, [], preLen);
                return 1 + sum;
            }
        }

        let add = 0;
        if(path.length == k) {
            add = 1;
            path = [];
        }
        
        
        let curr = stack[index];
        //index不用
        used[curr] = true;
        let next = path.map((value) => value);
        let sum1 = dfs(stack, inDegree, outList, used, index + 1, next, preLen);
        used[curr] = false;

        let sum2 = 0;
        //index使用 
        if(used[curr] == false) {
            let currOut = outList[curr];
            currOut.forEach((value) => {
                inDegree[value]--;
            })
            inDegree[curr] = -1;
            used[curr] = true;
            let nextPath = path.map((value) => value);
            nextPath.push(curr);
            sum2 = dfs(stack, inDegree, outList, used, index + 1, nextPath, preLen + 1);
            used[curr] = false;
            currOut.forEach((value) => {
                inDegree[value]++;
            })
            inDegree[curr] = 0;
        }
        let sum = add + Math.min(sum1, sum2);
        // console.log(`sum1 ${sum1} sum2 ${sum2} ${sum}`);
        return sum;
    }

    let used = new Array(n + 1).fill(false);
    let path = [];
    let res = dfs(stack, inDegree, outList, used, 0, path, 0);
    return res;

}


n = 4, relations = [[2,1],[3,1],[1,4]], k = 3;
// n = 5, relations = [[2,1],[3,5],[4,1],[1,5]], k = 2;

n = 13;
relations = [[12,8],[2,4],[3,7],[6,8],[11,8],[9,4],[9,7],[12,4],[11,4],[6,4],[1,4],[10,7],[10,4],[1,7],[1,8],[2,7],[8,4],[10,8],[12,7],[5,4],[3,4],[11,7],[7,4],[13,4],[9,8],[13,8]];
k = 9;

n = 7;
relations = [];
k = 2;

let label = 'minNumberOfSemesters';
console.time(label);
// console.log(minNumberOfSemesters2(n,relations, k));
console.timeLog(label, 'minNumberOfSemesters2');
console.log(minNumberOfSemesters(n,relations, k));
console.timeEnd(label);