/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} vals
 * @param {number[][]} edges
 * @return {number}
 */
//TLE dfs 123 / 131 个通过测试用例
var numberOfGoodPaths2 = function(vals, edges) {
    let n = vals.length;
    let sum = n;

    let outList = new Array(n).fill(0).map(() => new Set());
    for (let i = 0; i < edges.length; i++) {
        let edge = edges[i];
        outList[edge[0]].add(edge[1]);
        outList[edge[1]].add(edge[0]);
    }

    let dfs = (currPos, used, beginPos, dstValue) => {
        let sum = 0;
        let currList = Array.from(outList[currPos]);
        for(let i = 0; i < currList.length; i++) {
            if(vals[currList[i]] <= dstValue && used[currList[i]] == false) {
                if(vals[currList[i]] == dstValue && beginPos < currList[i]) {
                    sum++;
                }
                used[currList[i]] = true;
                sum += dfs(currList[i], used, beginPos, dstValue);
                used[currList[i]] = false;
            }
        }
        return sum;
    }

    let used = new Array(n).fill(false);
    for(let i = 0; i < n; i++) {
        used[i] = true;
        let currSum = dfs(i, used, i, vals[i]);
        sum += currSum;
        used[i] = false;
        //console.log(`${i} ${currSum}`);
    }
    return sum;

};

var numberOfGoodPaths = function(vals, edges) {

    let n = vals.length;
    let father = new Array(n).fill(0);
    for(let i = 0; i < n; i++) {
        father[i] = i;
    }
    
    //查找father
    var find = function(father, u) {
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

    let outList = new Array(n).fill(0).map(() => new Set());
    for (let i = 0; i < edges.length; i++) {
        let edge = edges[i];
        outList[edge[0]].add(edge[1]);
        outList[edge[1]].add(edge[0]);
    }

    let allPair = vals.map((value,index) => [index, value]);
    allPair.sort((a,b) => { return a[1] - b[1]});
    console.log(allPair.join(' '));

    let sum = n;

    let used = new Array(n).fill(false);
    for(let i = 0; i < n; i++) {
        let curr = allPair[i];
        if(used[curr[1]] == true) {
            continue;
        }
        for(let j = 0; j < n; j++) {
            father[j] = j;
        }
        for(let j = 0; j < outList[curr[0]].length; i++) {
            if(vals[curr[0]] > vals[outList[curr[0]][j]]) {
                join(father, curr[0], vals[outList[curr[0]][j]]);
            }
        }

        //计算连通节点数目
        let rootMap = new Map();
        let nums = new Array(n).fill(0);
        for(let i = 0; i < father.length; i++) {
            //这里是节点合并
            let root = find(father,father[i])
            let count = rootMap.get(root);
            if(count == null) {
                count = 0;
            }
            rootMap.set(root,count + 1);
        }



        

    }



    

}

vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]];
// vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]];
console.log(numberOfGoodPaths(vals, edges));