/*
* auther yeling
* 558. 四叉树交集
* 
*/

/**
 * // Definition for a QuadTree node.
 * function Node(val,isLeaf,topLeft,topRight,bottomLeft,bottomRight) {
 *    this.val = val;
 *    this.isLeaf = isLeaf;
 *    this.topLeft = topLeft;
 *    this.topRight = topRight;
 *    this.bottomLeft = bottomLeft;
 *    this.bottomRight = bottomRight;
 * };
 */


function Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight) {
    this.val = val;
    this.isLeaf = isLeaf;
    this.topLeft = topLeft;
    this.topRight = topRight;
    this.bottomLeft = bottomLeft;
    this.bottomRight = bottomRight;
};
/**
 * @param {Node} quadTree1
 * @param {Node} quadTree2
 * @return {Node}
 */
var intersect = function (quadTree1, quadTree2) {
    let res = new Node();
    dfs(quadTree1, quadTree2, res);
};

var dfs = function (quadTree1, quadTree2, resTree) {
    if (quadTree1.isLeaf == 0 && quadTree2.isLeaf == 0) {
        resTree.isLeaf = 0;
        resTree.val = 0;
        resTree.topLeft = new Node();
        dfs(quadTree1.topLeft, quadTree2.topLeft, resTree.topLeft);

        resTree.topRight = new Node();
        dfs(quadTree1.topRight, quadTree2.topRight, resTree.topRight);

        resTree.bottomLeft = new Node();
        dfs(quadTree1.bottomLeft, quadTree2.bottomLeft, resTree.bottomLeft);

        resTree.bottomRight = new Node();
        dfs(quadTree1.bottomRight, quadTree2.bottomRight, resTree.bottomRight);

        if (resTree.topLeft != null && resTree.topLeft.isLeaf == 1 && resTree.topLeft.val == 1
            && resTree.topRight != null && resTree.topRight.isLeaf == 1 && resTree.topRight.val == 1
            && resTree.bottomLeft != null && resTree.bottomLeft.isLeaf == 1 && resTree.bottomLeft.val == 1
            && resTree.bottomRight != null && resTree.bottomRight.isLeaf == 1 && resTree.bottomRight.val == 1) {
            resTree.isLeaf = 1;
            resTree.val = 1;
            resTree.topLeft = null;
            resTree.topRight = null;
            resTree.bottomLeft = null;
            resTree.bottomRight = null;
        }

        if (resTree.topLeft != null && resTree.topLeft.isLeaf == 1 && resTree.topLeft.val == 0
            && resTree.topLeft != null && resTree.topRight.isLeaf == 1 && resTree.topRight.val == 0
            && resTree.topLeft != null && resTree.bottomLeft.isLeaf == 1 && resTree.bottomLeft.val == 0
            && resTree.topLeft != null && resTree.bottomRight.isLeaf == 1 && resTree.bottomRight.val == 0) {
            resTree.isLeaf = 1;
            resTree.val = 0;
            resTree.topLeft = null;
            resTree.topRight = null;
            resTree.bottomLeft = null;
            resTree.bottomRight = null;
        }

    } else if (quadTree1.isLeaf == 1 && quadTree2.isLeaf == 0) {
        if (quadTree1.val == 1) {
            resTree.isLeaf = 1;
            resTree.val = 1;
        } else if (quadTree1.val == 0) {
            resTree.isLeaf = quadTree2.isLeaf;
            resTree.val = quadTree2.val;
            resTree.topLeft = quadTree2.topLeft;
            resTree.topRight = quadTree2.topRight;
            resTree.bottomLeft = quadTree2.bottomLeft;
            resTree.bottomRight = quadTree2.bottomRight;
        }
    } else if (quadTree2.isLeaf == 1 && quadTree1.isLeaf == 0) {
        if (quadTree2.val == 1) {
            resTree.isLeaf = 1;
            resTree.val = 1;
        } else if (quadTree2.val == 0) {
            resTree.isLeaf = quadTree1.isLeaf;
            resTree.val = quadTree1.val;
            resTree.topLeft = quadTree1.topLeft;
            resTree.topRight = quadTree1.topRight;
            resTree.bottomLeft = quadTree1.bottomLeft;
            resTree.bottomRight = quadTree1.bottomRight;
        }
    } else if (quadTree2.isLeaf == 1 && quadTree1.isLeaf == 1) {
        resTree.isLeaf = 1;
        resTree.val = quadTree2.val || quadTree1.val;
    }


}
