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