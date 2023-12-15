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
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var evaluateTree = function(root) {
    let dfs = function(root) {
        if(root.left == null &&  root.right == null) {
            return root.val == 1;
        }
        let left = dfs(root.left);
        let right = dfs(root.right);
        let ret = false;
        if(root.val == 2) {
            ret = left | right;
        } else if(root.val == 3) {
            ret = left & right;
        }
        return ret;
    }
    let ret = dfs(root);
    return ret;
};

evaluateTree(null);