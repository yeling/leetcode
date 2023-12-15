/*
* auther yeling
* 623. 在二叉树中增加一行
* 
*/

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @param {number} val
 * @param {number} depth
 * @return {TreeNode}
 */
var addOneRow = function (root, val, depth) {
    let stack = new Array();
    stack.push(root);
    let currDepth = 1;
    while (true) {
        if(depth == 1) {
            let temp = new TreeNode(val, root, null);
            root = temp;
            break;
        }
        currDepth++;
        let len = stack.length;
        if (currDepth == depth) {
            while (len > 0) {
                let top = stack.shift();
                
                let temp = new TreeNode(val, top.left, null);
                top.left = temp;

                temp = new TreeNode(val, null, top.right);
                top.right = temp;

                len--;

            }
            break;
        }
        while (len > 0) {
            let top = stack.shift();
            if (top.left != null) {
                stack.push(top.left);
            }
            if (top.right != null) {
                stack.push(top.right);
            }
            len--;
        }
    }
    return root;
};

let head = new TreeNode(3);
head.left = new TreeNode(2);
head.right = new TreeNode(3);

let res = addOneRow(head,1,1)
console.log(res);