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
var minimumOperations = function(root) {

    let calc = (nums) => {
        //选择排序
        count = 0;
        for(let i = 0; i < nums.length; i++) {
            let min = nums[i];
            let minIndex = i;
            for(let j = i + 1; j < nums.length; j++) {
                if(nums[j] < min) {
                    min = nums[j];
                    minIndex = j;
                }
            }
            if(minIndex != i) {
                let temp = nums[i]
                nums[i] = nums[minIndex];
                nums[minIndex] = temp;
                count++;
            }
        }
        return count;
    }

    let stack = new Array();
    stack.push(root);
    let sum = 0;
    while(stack.length > 0) {
        let count = stack.length;
        let vals = [];
        for(let i = 0; i < count; i++) {
            let curr = stack.shift();
            vals.push(curr.val)
            if(curr.left != null) {
                stack.push(curr.left);
            }
            if(curr.right != null) {
                stack.push(curr.right);
            }
        }
        sum += calc(vals);
    }
    return sum;

};

let head = new TreeNode(3);
head.left = new TreeNode(2);
head.right = new TreeNode(3);

head.right.right = new TreeNode(1);
head.left.right = new TreeNode(3);

// console.log(`${rob(head)}`);

console.log(`${minimumOperations(head)}`);