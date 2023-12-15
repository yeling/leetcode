/*
* auther yeling
* 1192. 查找集群内的「关键连接」
* 
*/

/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number[][]}
 */
//TLE 并查集遍历每条边 0(n^2) 9 / 17 个通过测试用例
var criticalConnections2 = function (n, connections) {
    let check = (subConnections, used) => {
        //father数组初始化
        let father = new Array(n);
        for (let i = 0; i < n; i++) {
            father[i] = i;
        }

        //查找father
        var find = function (father, u) {
            if (father[u] != u) {
                father[u] = find(father, father[u])
            }
            return father[u];
        }

        //合并
        var join = function (father, u, v) {
            let fu = find(father, u);
            let fv = find(father, v);
            if (fu != fv) {
                father[fu] = fv;
            }
        }

        for (let i = 0; i < subConnections.length; i++) {
            if(used[i]) {
                join(father, subConnections[i][0], subConnections[i][1]);
            }            
        }

        //计算连通节点数目
        let rootMap = new Map();
        for (let i = 0; i < father.length; i++) {
            //这里是节点合并
            let root = find(father, father[i])
            let count = rootMap.get(root);
            if (count == null) {
                count = 0;
            }
            rootMap.set(root, count + 1);
        }
        // console.log(subConnections.join(' '));
        // console.log(rootMap);
        if (rootMap.size > 1) {
            return true;
        } else {
            return false;
        }
    }
    let res = [];
    let used = new Array(connections.length).fill(true);
    for (let i = 0; i < connections.length; i++) {
        used[i] = false;        
        if (check(connections, used) ) {
            res.push(connections[i]);
        }
        used[i] = true;        
    }
    return res;
};

var criticalConnections = function (n, connections) {
    let res = [];
    let dfn = new Array(n).fill(-1);
    let low = new Array(n).fill(n);
    let num = 0;
    let dfs = (allPos, index, father) => {
        console.log(`dfs ${index}`);      
        if(dfn[index] == -1) {
            dfn[index] = num++;
            low[index] = dfn[index];
        } 
        let childs = allPos[index];
        for(let i = 0; i < childs.length; i++) {
            if(low[childs[i]] == n) {
                dfs(allPos, childs[i], index);
                low[index] = Math.min(low[index], low[childs[i]]);
            } else if(childs[i] != father){
                low[index] = Math.min(low[index], low[childs[i]]);
            }            
        }
        console.log(dfn);
        console.log(low);
        return low[index]

    }
    let allPos = new Array(n).fill(0).map(() => []);
    for(let i = 0; i < connections.length; i++) {
        allPos[connections[i][0]].push(connections[i][1]);
        allPos[connections[i][1]].push(connections[i][0]);
    }
    
    console.log(allPos);
    dfs(allPos, 0, -1);
    console.log(dfn);
    console.log(low);

    for(let i = 0; i < connections.length; i++) {
        let curr = connections[i];
        if(dfn[curr[0]] < low[curr[1]] || dfn[curr[1]] < low[curr[0]]) {
            res.push(curr);
        }
    }

    return res;
}

n = 4, connections = [[0, 1], [1, 2], [2, 0], [1, 3]];
// n = 5
// connections = [[1,0],[2,0],[3,2],[4,2],[4,3],[3,0],[4,0]]
// n = 2, connections = [[0,1]]

console.log(criticalConnections2(n, connections).join(' '));
console.log('======');
console.log(criticalConnections(n, connections).join(' '));