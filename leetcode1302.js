/*
* auther yeling
* 1302. 层数最深叶子节点的和
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
 * @return {number}
 */
var deepestLeavesSum = function(root) {
    let stack = new Array();
    stack.push(root);
    let sum = 0;
    while(stack.length > 0) {
        let len = stack.length;
        sum = 0;
        for(let i = 0; i < len; i++) {
            let temp = stack.shift();
            sum += temp.val;
            if(temp.left != null) {
                stack.push(temp.left);
            }
            if(temp.right != null) {
                stack.push(temp.right);
            }
        }
    }
    return sum;
};
