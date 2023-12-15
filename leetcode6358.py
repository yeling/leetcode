
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Node:
    def __init__(self):
        self.val = 0
        self.add = 0
        self.left = None
        self.right = None
        return
    
class SegmentTreeDynamic:
    def __init__(self, n):
        self.N = n
        self.root = Node()

    def update(self,  node, start, end, l, r, val):
        # print('update', start, end, l, r, (start + end) >> 1, val)
        if l <= start and end <= r:
            node.val += val
            # node.val += (end - start + 1) * val
            node.add += val
            return 
        
        mid = (start + end) >> 1
        self.pushDown(node, mid - start + 1, end - mid)
        if l <= mid: self.update(node.left, start, mid, l, r, val)
        if r > mid: self.update(node.right, mid + 1, end, l, r, val)
        self.pushUp(node)
    

    def query(self, node, start, end, l, r):
        # print('query', start, end, l, r, (start + end) >> 1, node.val, node.add)
        if l <= start and end <= r:
            return node.val
        mid = (start + end) >> 1
        ans = 0
        self.pushDown(node, mid - start + 1, end - mid)
        if l <= mid: ans = self.query(node.left, start, mid, l, r)
        if r > mid: ans = self.query(node.right, mid + 1, end, l, r)
        return ans
        
    def pushUp(self, node):
        return
        # node.val = min(node.left.val , node.right.val)
    
    def pushDown(self, node, leftNum, rightNum):
        if node.left == None: node.left = Node()
        if node.right == None: node.right = Node()
        if node.add == 0: return 
        node.left.val += node.add
        node.right.val += node.add
        # # 对区间进行「加减」的更新操作，下推懒惰标记时需要累加起来，不能直接覆盖
        node.left.add += node.add
        node.right.add += node.add
        node.add = 0


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        tree = SegmentTreeDynamic(n)
        preSum = sum(nums2)
        ans = []
        for v,p,q in queries:
            if v == 1:
                tree.update(tree.root, 0, tree.N, p, q, 1)
            elif v == 2:
                temp = tree.query(tree.root, 0, tree.N, q, q)
                if temp%2 == 0 and nums1[]
                preSum += temp

        return
    
nums1 = [1,0,1]
nums2 = [0,0,0]
queries = [[1,1,1],[2,1,0],[3,0,0]]

sol = Solution()
print(sol.handleQuery(nums1, nums2, queries))
