/*
* auther yeling
* 919. 完全二叉树插入器
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
 */
var CBTInserter = function (root) {
    this.root = root;
    let stack = new Array();
    stack.push(root);
    while(stack.length > 0) {
        let len = stack.length, i = 0;
        while(i < len) {
            let temp = stack.at(i);
            if(temp.left != null) {
                stack.push(temp.left);
            } else {
                break;
            }
            if(temp.right != null) {
                stack.push(temp.right);
            } else {
                break;
            }
            i++;
            console.log(temp.val);
        }
        
        //长度没有增长的情况
        if(stack.length == len) {
            this.bLayer = stack;
            this.bIndex = 0;
            break;
        }
        //没有遍历完，遇到空节点
        if(i != len) {
            stack.splice(len,stack.length - len);
            this.bLayer = stack;
            this.bIndex = i;
            break;
        }
        stack.splice(0,len);
        //console.log(stack.length);
    }
};

/** 
 * @param {number} val
 * @return {number}
 */
CBTInserter.prototype.insert = function (val) {
    let curr = new TreeNode(val);
    if (this.bIndex < this.bLayer.length) {
        let father = this.bLayer.at(this.bIndex);
        if (father.left == null) {
            father.left = curr;
        } else if (father.right == null) {
            father.right = curr;
            this.bIndex++;
        }
        return father.val;
    } else {
        let len = this.bLayer.length;
        while (len > 0) {
            let temp = this.bLayer.shift();
            if (temp.left != null) {
                this.bLayer.push(temp.left);
            }
            if (temp.right != null) {
                this.bLayer.push(temp.right);
            }
            len--;
            console.log(temp.val);
        }
        this.bIndex = 0;
        this.bLayer[0].left = curr;
        return this.bLayer[0].val;
    }
};

/**
 * @return {TreeNode}
 */
CBTInserter.prototype.get_root = function () {
    return this.root;
};

/**
 * Your CBTInserter object will be instantiated and called as such:
 * var obj = new CBTInserter(root)
 * var param_1 = obj.insert(val)
 * var param_2 = obj.get_root()
 */

 let head = new TreeNode(1);
 head.left = new TreeNode(2);
//  head.right = new TreeNode(3);
 
//  head.left.right = new TreeNode(4);
//  head.left.left = new TreeNode(5);
//  head.right.left = new TreeNode(6);
 


let cBTInserter = new CBTInserter(head);
console.log(cBTInserter.insert(3));  // 返回 4
console.log(cBTInserter.insert(4));  // 返回 4
console.log(cBTInserter.insert(5));  // 返回 3
console.log(cBTInserter.insert(6));  // 返回 3
cBTInserter.get_root(); // 返回 [1, 2, 3, 4]

