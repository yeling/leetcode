/*
* auther yeling
* 
* 
*/
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} restricted
 * @return {number}
 */
var reachableNodes = function (n, edges, restricted) {
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

    let resSet = new Set(restricted);
    //console.log(resSet);
    for(let i = 0; i < edges.length; i++) {
        let temp = edges[i];
        if(resSet.has(temp[0]) == false && resSet.has(temp[1]) == false) {
            join(father,temp[1],temp[0]);
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
    //console.log(rootMap);
    let root = find(father,0);
    return rootMap.get(root);

};



n = 7, edges = [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], restricted = [4, 5]


console.log(reachableNodes(n,edges,restricted));