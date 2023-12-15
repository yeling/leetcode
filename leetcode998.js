/*
* auther yeling
* 998. 最大二叉树 II
* 
*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @param {number} val
 * @return {TreeNode}
 */
var insertIntoMaxTree = function (root, val) {
    let nums = treeToArray(root);
    console.log(nums);
    nums.push(val);
    return constructMaximumBinaryTree(nums);
};

var treeToArray = (head) => {
    let res = [];
    res.push(head.val);
    if(head.left != null) {
        res.splice(0,0,...treeToArray(head.left));
    }
    if(head.right != null) {
        res.push(...treeToArray(head.right))
    }
    return res;
}

var constructMaximumBinaryTree = function(nums) {
    let dfs = function(array) {
        //console.log(array);
        let max = array[0];
        let maxIndex = 0;
        for(let i = 0; i < array.length; i++) {
            if(max < array[i]) {
                max = array[i];
                maxIndex = i;
            }
        }

        let head = new TreeNode(max);
        if(maxIndex > 0) {
            head.left = dfs(array.slice(0,maxIndex));
        }
        if(maxIndex < array.length - 1) {
            head.right =  dfs(array.slice(maxIndex + 1));
        }
        return head;

    }

    return dfs(nums);
};

let nums = [2,1,5,4,3];

let root = constructMaximumBinaryTree(nums);
let res = insertIntoMaxTree(root,6);
console.log(treeToArray(res));

