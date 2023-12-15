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
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}


/**
 * @param {TreeNode} root
 * @return {number}
 */
//72 / 114 个通过测试用例 TLE
//94 / 114 个通过测试用例
var widthOfBinaryTree = function (root) {

    let stack = new Array();
    stack.push(root);
    let maxWidth = 1;
    while (stack.length > 0) {
        let count = stack.length;
        let begin = -1, end = -1;
        for (let i = 0; i < count; i++) {
            let curr = stack.shift();
            if (curr == '#') {
                stack.push('#');
                stack.push('#');
            } else {
                if (begin == -1) {
                    begin = i;
                }
                end = i;
                if (curr.left != null) {
                    stack.push(curr.left);
                } else {
                    stack.push('#');
                }
                if (curr.right != null) {
                    stack.push(curr.right);
                } else {
                    stack.push('#');
                }
            }
        }
        while (stack.length > 0 && stack[stack.length - 1] == '#') {
            stack.pop();
        }
        while (stack.length > 0 && stack[0] == '#') {
            stack.shift();
        }

        if (begin == -1) {
            break;
        }
        maxWidth = Math.max(maxWidth, end - begin + 1);
    }
    return maxWidth;

};

//111 / 114 
var widthOfBinaryTree2 = function (root) {
    let stack = new Array();
    let posStack = new Array();
    stack.push(root);
    posStack.push(0n);
    let maxWidth = 1n;
    while (stack.length > 0) {
        let space = posStack[posStack.length - 1] - posStack[0] + 1n;
        if(space > maxWidth) {
            maxWidth = space;
        }
        let count = stack.length;
        for (let i = 0; i < count; i++) {
            let curr = stack.shift();
            let pos = posStack.shift();
            if (curr.left != null) {
                stack.push(curr.left);
                posStack.push(2n * pos);
            }
            if (curr.right != null) {
                stack.push(curr.right);
                posStack.push(2n * pos + 1n);
            }
        }
    }
    return maxWidth;

};
//root = [3,2,3,null,3,null,1]

let head = new TreeNode(1);
// head.left = new TreeNode(3);
head.right = new TreeNode(2);

// head.left.left = new TreeNode(5);
// head.left.right = new TreeNode(3);


head.right.left = new TreeNode(3);
head.right.right = new TreeNode(9);

// console.log(`${rob(head)}`);

console.log(`${widthOfBinaryTree(head)}`);
console.log(`${widthOfBinaryTree2(head)}`);