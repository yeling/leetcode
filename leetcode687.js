/*
* auther yeling
* 687. 最长同值路径
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
//PASS
 var longestUnivaluePath = function(root) {
    let max = 0;
    let dfs = (head) => {
        //console.log(head);
        if(head == null) {
            return 0;
        }
        let len = 0;
        let leftLen = dfs(head.left); 
        let rightLen = dfs(head.right);
        if(head.left == null) {
            if(head.right != null && head.val == head.right.val) {
                len =  1 + rightLen;
                max = Math.max(max,len);
            }
        } else if(head.right == null) {
            if(head.left != null && head.val == head.left.val) {
                len =  1 + leftLen;
                max = Math.max(max,len);
            }
        } else {
            if(head.val == head.left.val && head.val == head.right.val) {
                len = 1 + Math.max(leftLen, rightLen);
                max = Math.max(max,leftLen + rightLen + 2); 
            } else if(head.val == head.left.val) {
                len =  1 + leftLen;
                max = Math.max(max,len);
            } else if(head.val == head.right.val) {
                len =  1 + rightLen;
                max = Math.max(max,len);
            }
        }
        return len;
    }
    dfs(root);
    return max;
};


//root = [1,2,2,2,2]
//[1,null,1,1,1,1,1,1]

let head = new TreeNode(1);
head.left = new TreeNode(2);
head.right = new TreeNode(2);

head.left.right = new TreeNode(2);
head.left.left = new TreeNode(2);

console.log(longestUnivaluePath(head));
