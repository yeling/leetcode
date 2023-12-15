/*
* auther yeling
* 
* 
*/

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}
/**
 * @param {TreeNode} root
 * @param {number[]} queries
 * @return {number[]}
 */

var treeQueries2 = function(root, queries) {
    //增加 lh rh h father
    let dfs = (root) => {
        let h = -1;
        if(root.left != null) {
            root.left.f = root;
            root.lh = dfs(root.left);
            h = Math.max(h, root.lh);
        }
        if(root.right != null) {
            root.right.f = root;
            root.rh = dfs(root.right);
            h = Math.max(h, root.rh);
        }
        root.h = h + 1;
        return root.h;
    }
    dfs(root);
    let res = [];
   
    for(let i = 0; i < queries.length; i++) {
        let target = queries[i];
        let stack = new Array();
        stack.push(root);
        let len = 0;
        while(stack.length > 0) {
            let count = stack.length;
            for(let i = 0; i < count; i++) {
                let curr = stack.shift();
                if(curr.val != target) {
                    if(curr.left != null) {
                        stack.push(curr.left);
                    }
                    if(curr.right != null) {
                        stack.push(curr.right);
                    }
                }
            }
            len++;
        }
        res.push(len);
    }

};

//TLE
//34 / 39 个通过测试用例
var treeQueries3 = function(root, queries) {
    //增加 lh rh h father
    let res = [];
    for(let i = 0; i < queries.length; i++) {
        let target = queries[i];
        let stack = new Array();
        stack.push(root);
        let len = -1;
        while(stack.length > 0) {
            let count = stack.length;
            let find = 0;
            for(let i = 0; i < count; i++) {
                let curr = stack.shift();
                if(curr.val != target) {
                    if(curr.left != null) {
                        stack.push(curr.left);
                    }
                    if(curr.right != null) {
                        stack.push(curr.right);
                    }
                } else {
                    find++;
                }
            }
            len++;
            if(find == count && stack.length == 0) {
                len--;
            }
        }
        res.push(len);
    }
    // console.log(res);
    return res;
};

//TLE
//34 / 39 个通过测试用例
//PASS 引入缓存，因为每个值都不一样
//两次dfs
var treeQueries = function(root, queries) {
    //增加 lh rh h father
    let cache = new Array(10 ** 5).fill(0);
    let dfs = (root) => {
        cache[root.val] = root;
        let h = -1;
        if(root.left != null) {
            root.left.f = root;
            root.lh = dfs(root.left);
            h = Math.max(h, root.lh);
        } else {
            root.lh = -1;
        }
        if(root.right != null) {
            root.right.f = root;
            root.rh = dfs(root.right);
            h = Math.max(h, root.rh);
        } else {
            root.rh = -1;
        }
        root.h = h + 1;
        return root.h;
    }
    dfs(root);
    let res = [];
    for(let i = 0; i < queries.length; i++) {
        let target = cache[queries[i]];
        let back = -1;
        let len = 0;
        while(target.f != null) {
            let f = target.f;
            let newh = -1;
            if(target == f.right) {
                newh = Math.max(f.lh, back) + 1;
            } else if(target == f.left) {
                newh = Math.max(f.rh, back) + 1;
            }
            
            if(newh == f.h) {
                back = root.h;
                target = root;
                break;
            } else {
                back = newh;
                target = f;
            }
        }
        len = back;
        res.push(len);
    }
    return res;
};
//root = [3,2,3,null,3,null,1]

let head = new TreeNode(1);
// head.left = new TreeNode(8);
head.right = new TreeNode(5);

// head.right.right = new TreeNode(7);
head.right.left = new TreeNode(3);

// head.left.right = new TreeNode(1);
// head.left.left = new TreeNode(2);

queries = [3,5]

console.log(treeQueries(head,queries));
