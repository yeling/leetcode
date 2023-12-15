from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

class RBNnode:
    def __init__(self, val, color="R"):
        self.val = val
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def is_black_node(self):
        return self.color == "B"

    def set_black_node(self):
        self.color = "B"

    def set_red_node(self):
        self.color = "R"
    
    def print(self):
        if self.left:
            self.left.print()
        print(self.val)
        if self.right:
            self.right.print()

class RBTree:
    '''
    红黑树 五大特征
    性质一：节点是红色或者是黑色；
    性质二：根节点是黑色；
    性质三：每个叶节点（NIL或空节点）是黑色；
    性质四：每个红色节点的两个子节点都是黑色的（也就是说不存在两个连续的红色节点）；
    性质五：从任一节点到其没个叶节点的所有路径都包含相同数目的黑色节点
    '''
    def __init__(self):
        self.root = None

    def left_rotate(self, node):
        print("left rotate", node.val)
        '''
        * 左旋示意图:对节点x进行左旋
        *     parent               parent
        *    /                       /
        *   node                   right
        *  / \                     / \
        * ln  right   ----->     node  ry
        *    / \                 / \
        *   ly ry               ln ly
        * 左旋做了三件事：
        * 1. 将right的左子节点ly赋给node的右子节点,并将node赋给right左子节点ly的父节点(ly非空时)
        * 2. 将right的左子节点设为node，将node的父节点设为right
        * 3. 将node的父节点parent(非空时)赋给right的父节点，同时更新parent的子节点为right(左或右)
        :param node: 要左旋的节点
        :return:
        '''
        parent = node.parent
        right = node.right

        # 把右子节点的左子节点，赋给右节点
        node.right = right.left
        if node.right:
            node.right.parent = node

        # 把node变成基右子节点的左子节点
        right.left = node
        node.parent = right

        # 右子节点的父节点更新为原来节点的父节点
        right.parent = parent
        if not parent:
            self.root = right
        else:
            if parent.left == node:
                parent.left = right
            else:
                parent.right = right

    def right_rotate(self, node):
        print("right rotate", node.val)
        '''
        * 左旋示意图：对节点y进行右旋
        *        parent           parent
        *       /                   /
        *      node                left
        *     /    \               / \
        *    left  ry   ----->   ln  node
        *   / \                     / \
        * ln  rn                   rn ry
        * 右旋做了三件事：
        * 1. 将left的右子节点rn赋给node的左子节点,并将node赋给rn右子节点的父节点(left右子节点非空时)
        * 2. 将left的右子节点设为node，将node的父节点设为left
        * 3. 将node的父节点parent(非空时)赋给left的父节点，同时更新parent的子节点为left(左或右)
        :param node:
        :return:
        '''
        parent = node.parent
        left = node.left

        # 将left的左子节点赋给node的左子节点
        if node.left:
            node.left = left.right
            node.left.parent = node

        # left的右子节点为node，node的父子节点为left
        left.right = node
        node.parent = left

        # 将left的父子节点更新为parent
        left.parent = parent
        if not parent:
            self.root = left
        else:
            if parent.left == node:
                parent.left = left
            else:
                parent.right = left