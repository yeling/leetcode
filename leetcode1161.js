/*
* auther yeling
* 1161. 最大层内元素和
* 
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
var maxLevelSum = function (root) {
    if (root == null) {
        return 0;
    }
    let head = root;
    let stack = new Array();
    let level = 1;
    stack.push(head);
    let sum = new Array();
    while (stack.length > 0) {
        let len = stack.length;
        let currSum = 0;
        for (let i = 0; i < len; i++) {
            let tmp = stack.shift();
            currSum += tmp.val;
            if (tmp.left != null) {
                stack.push(tmp.left);
            }
            if (tmp.right != null) {
                stack.push(tmp.right);
            }
        }
        sum.push({ val: currSum, level: level });
        level++;
    }
    sum.sort((a,b) => {
        if(a.val == b.val) {
            return a.level - b.level;
        } else {
            return b.val - a.val;
        }
    })
    return sum[0].level;
};


//root = [3,2,3,null,3,null,1]

let head = new TreeNode(1);
head.left = new TreeNode(7);
head.right = new TreeNode(0);

head.left.left = new TreeNode(7);
head.left.right = new TreeNode(-8);
console.log(maxLevelSum(head));