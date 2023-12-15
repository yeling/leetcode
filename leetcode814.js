/*
* auther yeling
* 
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
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var pruneTree = function(root) {
    if(dfs(root)) {
        return null;
    } else {
        return root;
    }
};

var dfs = function(root) {
    if(root == null) {
        return true;
    }
    if(root.left == null && root.right == null) {
        return root.val == 0;
    }
    
    if(dfs(root.left)) {
        root.left = null;
    }
    if(dfs(root.right)) {
        root.right = null;
    }
    if(root.left == null && root.right == null) {
        return root.val == 0;
    } else {
        return false;
    }
}

let head = new TreeNode(1);
head.left = new TreeNode(0);
head.right = new TreeNode(0);

head.right.right = new TreeNode(0);
head.right.left = new TreeNode(0);
head.left.right = new TreeNode(1);

console.log(pruneTree(head));