/*
* auther yeling
* 337. 打家劫舍 III
* 
*/

/**
 * Definition for a binary tree node.

 */
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}
/**
 * @param {TreeNode} root
 * @return {number}
 */
//122 / 124 个通过测试用例 超时
var rob = function (root) {
    let val = dfs(root, false);
    return val;
};

//不给内存
let cache = new Map();
var dfs = function (root, preTaken) {
    if(cache.get({ root, preTaken }) != null) {
        return cache.get({ root, preTaken });
    }
    if (root == null) {
        return 0;
    }
    let ret = 0;
    if (preTaken) {
        //当前节点不能取
        ret = dfs(root.left, false) + dfs(root.right, false);
    } else {
        //当前节点可以取
        let take = root.val + dfs(root.left, true) + dfs(root.right, true);
        let untake = dfs(root.left, false) + dfs(root.right, false);
        ret = Math.max(take, untake);
    }
    cache.set({ root, preTaken }, ret);
    return ret;
}

//动态规划
var rob2 = function (root) {
    //return [0,1] 0表示不取，1表示取
    let dfs = function (root) {
        if (root == null) {
            return [0,0];
        }
        let left = dfs(root.left);
        let right = dfs(root.right);

        let take = left[0] + right[0] + root.val;
        let untake = Math.max(left[0],left[1]) + Math.max(right[0],right[1]);
        return [untake,take];
    }
    let val = dfs(root);
    return Math.max(val[0],val[1]);
};

//root = [3,2,3,null,3,null,1]

let head = new TreeNode(3);
head.left = new TreeNode(2);
head.right = new TreeNode(3);

head.right.right = new TreeNode(1);
head.left.right = new TreeNode(3);

// console.log(`${rob(head)}`);

console.log(`${rob2(head)}`);