/*
* auther yeling
* 565. 数组嵌套
* 图论，最长路径，并查集
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayNesting = function(nums) {
    //father数组初始化
    let m = nums.length;
    let father = new Array(m);
    for(let i = 0; i < m; i++) {
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

    for(let i = 0; i < nums.length; i++) {
        join(father,i,nums[i]);
    }


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

    let ret = 0;
    rootMap.forEach((value)=>{
        ret = Math.max(ret,value);
    })
    return ret;

};

A = [5,4,0,3,1,6,2];
console.log(`${arrayNesting(A)}`);
