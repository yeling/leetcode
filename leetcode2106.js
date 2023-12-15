/*
* auther yeling
* 2106. 摘水果
* 
*/

/**
 * @param {number[][]} fruits
 * @param {number} startPos
 * @param {number} k
 * @return {number}
 */

 var Node = function(){
    this.left = null;
    this.right = null;
    this.val = null;
    this.add = null;
}

var SegmentTreeDynamic = function(){
    this.N = 10 ** 6;
    this.root = new Node();

    this.update = function(node, start, end, l, r, val) {
        if (l <= start && end <= r) {
            node.val += (end - start + 1) * val;
            node.add += val;
            return ;
        }
        let mid = (start + end) >> 1;
        this.pushDown(node, mid - start + 1, end - mid);
        if (l <= mid) this.update(node.left, start, mid, l, r, val);
        if (r > mid) this.update(node.right, mid + 1, end, l, r, val);
        this.pushUp(node);
    }

    this.query = function(node, start, end, l, r) {
        if (l <= start && end <= r) return node.val;
        let mid = (start + end) >> 1, ans = 0;
        this.pushDown(node, mid - start + 1, end - mid);
        if (l <= mid) ans += this.query(node.left, start, mid, l, r);
        if (r > mid) ans += this.query(node.right, mid + 1, end, l, r);
            return ans;
    }
    this.pushUp = function(node) {
        node.val = node.left.val + node.right.val;
    }
    this.pushDown = function( node, leftNum, rightNum) {
        if (node.left == null) node.left = new Node();
        if (node.right == null) node.right = new Node();
        if (node.add == 0) return ;
        node.left.val += node.add * leftNum;
        node.right.val += node.add * rightNum;
        // 对区间进行「加减」的更新操作，下推懒惰标记时需要累加起来，不能直接覆盖
        node.left.add += node.add;
        node.right.add += node.add;
        node.add = 0;
    }
}

var maxTotalFruits = function(fruits, startPos, k) {
    let tree = new SegmentTreeDynamic();

    for(let i = 0; i < fruits.length; i++) {
        tree.update(tree.root, 0, tree.N, fruits[i][0], fruits[i][0], fruits[i][1]);
    }

    let res = 0;
    let left = k;
    if(startPos - left <= 0) {
        left = startPos;
    }
    right = 0;
    left = Math.max(0, left);
    while(left >= 0) {
        if(k > 2 * left) {
            right = k - 2 * left;
        } else {
            right = 0;
        }
        let temp = tree.query(tree.root, 0, tree.N, startPos - left, startPos + right);
        res = Math.max(res,temp);
        left--;
    }

    right = k;
    left = 0;
    while(right >= 0) {
        if(k > 2 * right) {
            left = k - 2 * right;
        } else {
            left = 0;
        }
        if(left < 0) {
            left = 0;
        }
        let temp = tree.query(tree.root, 0, tree.N, startPos - left, startPos + right);
        res = Math.max(res,temp);
        right--;
    }
    return res;
};

fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4
fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
console.log(maxTotalFruits(fruits, startPos, k));
