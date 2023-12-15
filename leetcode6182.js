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
var reverseOddLevels = function(root) {
    let stack = new Array();
    stack.push(root);
    while(stack.length > 0) {
        let count = stack.length;
        for(let i = 0; i < count; i++) {
            let curr = stack[i];
            if(curr.left != null) {
                stack.push(curr.left);
            }
            if(curr.right != null) {
                stack.push(curr.right);
            }
        }
        let count2 = stack.length;
        for(let i = count; i < count2; i++) {
            let curr = stack[i];
            if(curr.left != null) {
                stack.push(curr.left);
            }
            if(curr.right != null) {
                stack.push(curr.right);
            }
        }

        for(let i = count - 1, j = count; i >= 0; i--) {
            if(j < count2) {
                stack[i].right = stack[j++];
            }
            if(j < count2) {
                stack[i].left = stack[j++];
            }
        }

        for(let i = count2 - 1, j = count2; i >= count ; i--) {
            if(j < stack.length) {
                stack[i].left = stack[j++];
            }
            if(j < stack.length) {
                stack[i].right = stack[j++];
            }
        }
        stack = stack.slice(count2);
    }

    return root;
};

let head = new TreeNode(3);
head.left = new TreeNode(2);
head.right = new TreeNode(1);

head.right.left = new TreeNode(5);
head.right.right = new TreeNode(4);
head.left.right = new TreeNode(6);
head.left.left = new TreeNode(7);
reverseOddLevels(head);
console.log(head);