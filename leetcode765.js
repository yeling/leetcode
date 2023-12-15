/*
* auther yeling
* 765. 情侣牵手
* 并查集
*/

/**
 * @param {number[]} row
 * @return {number}
 */
var minSwapsCouples = function (row) {
    let n = row.length / 2;
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

    for (let i = 0; i < row.length; i += 2) {
        join(father, Math.floor(row[i] / 2), Math.floor(row[i + 1] / 2));
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

    //console.log(father);

    let sum = 0;
    rootMap.forEach((value, key) => {
        sum += value - 1;
    })
    return sum;
};

row = [0, 2, 1, 3];
console.log(minSwapsCouples(row));

