/*
* auther yeling
* 331. 验证二叉树的前序序列化
* 先尝试重建二叉树
*/

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

//94 / 151
var isValidSerialization = function(preorder) {
    let nodeArray = preorder.split(',');
    //总节点奇数个，偶数个返回错误
    if(nodeArray.length%2 == 0) {
        return false;
    }
    if(nodeArray.length == 1 && preorder[0] == '#') {
        return true;
    }
    //console.log(nodeArray.join(''));
    let head = new TreeNode(nodeArray[0],null,null);
    let stack = new Array();
    let curr = head;
    stack.push(head);
    let i = 1;
    while(true) {
        if(curr == null || i == nodeArray.length) {
            break;
        } 
        //stack.push(curr);
        //console.log(curr);
        //console.log(stack);
        if(nodeArray[i] == '#') {
            if(curr.val == '#') {
                return false;
            }
            if(curr.left == null) {
                curr.left = new TreeNode('#');
            } else if(curr.right == null){
                curr.right = new TreeNode('#');
                stack.pop();
                curr = stack.pop();
                if(i == nodeArray.length - 1) {
                    return true;
                }
            }        
        } else {
            if(curr.left == null) {
                curr.left = new TreeNode(nodeArray[i]);
                curr = curr.left;
                stack.push(curr);
            } else {
                curr.right = new TreeNode(nodeArray[i]);
                curr = curr.right;
                stack.push(curr);
            }
        }
        i++;
    }
    return false;
};

//栈，槽位的概念，一个#消耗一个，一个数字先消耗1个，再增加连个2个
var isValidSerialization2 = function(preorder) {
    let nodeArray = preorder.split(',');
    let i = 0;
    let stack = [1];
    while(i < nodeArray.length) {
        if(stack.length == 0) {
            return false;
        }
        if(nodeArray[i] == '#') {
            stack[stack.length - 1]--;
            if(stack[stack.length - 1] == 0) {
                stack.pop();
            }
        } else {
            stack[stack.length - 1]--;
            if(stack[stack.length - 1] == 0) {
                stack.pop();
            }
            stack.push(2);
        }
        i++;
    }
    return stack.length == 0;
}

let preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#";
preorder = "9,2,#";
preorder = "#";
// preorder = "9,9,91,#,#,9,#,49,#,#,#";
// preorder = "1,#,#,#,#";
console.log(`${preorder}`);
// console.log(isValidSerialization(preorder));
console.log(isValidSerialization2(preorder));