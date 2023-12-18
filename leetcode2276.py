
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
from heapq import *
import string
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

# 73 / 73  TLE
# AC 7836ms

class Node:
    def __init__(self):
        self.val = 0
        self.add = 0
        self.left = None
        self.right = None
        return

class SegmentTreeDynamic:
    def __init__(self):
        self.N = 10 ** 9
        self.root = Node()

    def update(self,  node, start, end, l, r, val):
        if l <= start and end <= r:
            # 对区间进行「加减」的更新操作，需要 +=
            node.val = (end - start + 1) * val
            node.add += val
            return 
        
        mid = (start + end) >> 1
        self.pushDown(node, mid - start + 1, end - mid)
        if l <= mid: self.update(node.left, start, mid, l, r, val)
        if r > mid: self.update(node.right, mid + 1, end, l, r, val)
        self.pushUp(node)
    

    def query(self, node, start, end, l, r):
        if l <= start and end <= r:
            return node.val
        mid = (start + end) >> 1
        #注意区间和的表示方法
        ans = 0
        self.pushDown(node, mid - start + 1, end - mid)
        if l <= mid: ans += self.query(node.left, start, mid, l, r)
        if r > mid: ans += self.query(node.right, mid + 1, end, l, r)
        return ans
        
    def pushUp(self, node):
        #注意区间和的上推
        node.val = node.left.val + node.right.val
    
    def pushDown(self, node, leftNum, rightNum):
        if node.left == None: node.left = Node()
        if node.right == None: node.right = Node()
        if node.add == 0: return 
        
        node.left.val = leftNum
        node.right.val = rightNum
        # # 对区间进行「加减」的更新操作，下推懒惰标记时需要累加起来，不能直接覆盖
        node.left.add += node.add
        node.right.add += node.add
        node.add = 0

class CountIntervals:

    def __init__(self):
        self.tree = SegmentTreeDynamic()
        return

    def add(self, left: int, right: int) -> None:
        tree = self.tree
        tree.update(tree.root, 1, tree.N, left, right, 1)
        return

    def count(self) -> int:
        tree = self.tree
        cnt = tree.query(tree.root, 1, tree.N, 1, tree.N)
        return cnt



# Your CountIntervals object will be instantiated and called as such:
obj = CountIntervals()
obj.add(1,3)
obj.add(2,4)
obj.add(3,6)
c = obj.count()   
print(c) 
        
