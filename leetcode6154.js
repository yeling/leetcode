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
 * @param {number} start
 * @return {number}
 */
//70 / 79 个通过测试用例
var amountOfTime2 = function (root, start) {
    let stack = new Array();
    let dfs = function (curr, start) {
        //console.log('dfs ' + curr.val + ' ' + start);
        if (curr.val == start) {
            curr.infect = true;
            stack.push(curr);
        } else {
            curr.infect = false;
        }

        if (curr.left != null) {
            curr.left.father = curr;
            dfs(curr.left, start);
        }
        if (curr.right != null) {
            curr.right.father = curr;
            dfs(curr.right, start);
        }
    }

    //构建father,感染标志
    dfs(root, start);

    //BFS，开始感染
    let time = 0;
    while (stack.length > 0) {
        let count = 0;
        let len = stack.length;
        for (let i = 0; i < len; i++) {
            let curr = stack.shift();
            if (curr.right != null && curr.right.infect == false) {
                count++;
                curr.right.infect = true;
                stack.push(curr.right);
            }
            if (curr.left != null && curr.left.infect == false) {
                count++;
                curr.left.infect = true;
                stack.push(curr.left);
            }
            if (curr.father != null && curr.father.infect == false) {
                count++;
                curr.father.infect = true;
                stack.push(curr.father);
            }
        }
        if (count > 0) {
            time++;
        } else {
            break;
        }
    }
    return time;
};

var amountOfTime = function (root, start) {
    let stack = new Array();
    stack.push(root);
    let maxDepth = 0;
    let startDepth = 0;
    while (stack.length > 0) {
        let len = stack.length;
        for (let i = 0; i < len; i++) {
            let curr = stack.shift();
            if(curr.val == start) {
                startDepth = maxDepth;
            }
            if (curr.right != null ) {
                stack.push(curr.right);
            }
            if (curr.left != null ) {
                stack.push(curr.left);
            }
        }
        maxDepth++;
    }
    maxDepth--;
    //console.log(`${maxDepth} ${startDepth}`);
    let res = 0;
    if(startDepth == 0) {
        res = maxDepth;
    } else {
        res = startDepth + maxDepth;
    }
    return res;
};


let head = new TreeNode(3);
head.left = new TreeNode(2);
head.right = new TreeNode(1);

head.right.right = new TreeNode(4);
head.left.right = new TreeNode(5);

console.log(amountOfTime2(head,4));
console.log(amountOfTime(head,4));