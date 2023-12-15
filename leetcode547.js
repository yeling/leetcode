/*
* auther yeling
* 547. 省份数量
* 并查集
*/
/**
 * @param {number[][]} isConnected
 * @return {number}
 */
 var findCircleNum = function(isConnected) {
    let n = isConnected.length;
    let father = new Array(n);
    for(let i = 0; i < n; i++) {
        father[i] = i;
    }
    //console.log(father);
    for(let i = 0; i < n; i++) {
        for(let j = 0; j < n; j++) {
            if(isConnected[i][j] == 1) {
                join(father,i, j);
            }
        }
        // console.log(father);
    }
    //console.log(father);
    //计算连通节点数目
    let rootMap = new Map();
    for(let i = 0; i < father.length; i++) {
        //这里是节点合并
        let root = find(father,father[i])
        let count = rootMap.get(root);
        if(count == null) {
            count = 0;
        }
        rootMap.set(root,count + 1);
    }
    //console.log(rootMap.size);
    return rootMap.size;
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

