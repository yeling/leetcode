/*
* auther yeling
* 684. 冗余连接
* 
*/
/**
 * @param {number[][]} edges
 * @return {number[]}
 */
var findRedundantConnection = function(edges) {
    
    let n = edges[edges.length - 1][1];
    for(let i = 0; i < edges.length; i++) {
        n = Math.max(n,edges[i][1]);
    }
    //console.log(n);
    let father = new Array(n+1);
    //father.fill(0)
    for(let i = 0; i < father.length; i++) {
        father[i] = i;
    }
    for(let i = 0; i < edges.length; i++) {
        console.log(edges[i]);
        console.log(father);
        //join(father,edges[i][0],edges[i][1]);
        //join的动作
        let u = edges[i][0];
        let v = edges[i][1];
        let fu = find(father,u);
        let fv = find(father,v);
        if(fu != fv) {
            father[fu] = fv;
        } else {
            return edges[i];
        }
    }
    return null;
};

//查找father
var find = function(father, u) {
    if(father[u] != u) {
        //father[u] = find(father,father[u])
        return find(father,father[u])
    }
    return father[u];
}

//合并
var join = function(father, u, v) {
    let fu = find(father,u);
    let fv = find(father,v);
    if(fu != fv) {
        father[fu] = fv;
    } else {
        console.log(`join find ${u} ${v}`);
    }
}

let edges = [[1,2], [2,3], [3,4], [1,4], [1,5]];
edges = [[1,2], [1,3], [2,3]];
edges = [[1,3],[3,4],[1,5],[3,5],[2,3]]
console.log(`result ${findRedundantConnection(edges)}`);
