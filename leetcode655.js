/*
* auther yeling
* 655. 输出二叉树
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
 * @return {string[][]}
 */
var printTree = function (root) {
    let stack = new Array();
    stack.push(root);
    let depth = 0;
    while (stack.length > 0) {
        let len = stack.length;
        depth++;
        for (let i = 0; i < len; i++) {
            let curr = stack.shift();
            if (curr.right != null) {
                stack.push(curr.right);
            }
            if (curr.left != null) {
                stack.push(curr.left);
            }
        }
    }
    depth--;

    let matrix = new Array(depth + 1).fill(0).map(() => new Array(2 ** (depth + 1) - 1).fill(''));

    let dfs = function (curr, i, j, matrix, depth) {
        if (curr.left != null) {
            matrix[i + 1][j - 2 ** (depth - i - 1)] = "" + curr.left.val;
            dfs(curr.left, i + 1, j - 2 ** (depth - i - 1), matrix, depth);
        }
        if (curr.right != null) {
            matrix[i + 1][j + 2 ** (depth - i - 1)] = "" + curr.right.val;
            dfs(curr.right, i + 1, j + 2 ** (depth - i - 1), matrix, depth);
        }
    }

    matrix[0][Math.floor(matrix[0].length / 2)] = "" + root.val;
    dfs(root, 0, Math.floor(matrix[0].length / 2), matrix, depth);

    return matrix;
};

let head = new TreeNode(3);
head.left = new TreeNode(2);
head.right = new TreeNode(1);

head.right.right = new TreeNode(4);
head.left.right = new TreeNode(5);

let res = printTree(head)
console.log(res.join('\n'));