
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

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Node:
    def __init__(self):
        self.val = 0
        self.add = 0
        self.l = 0
        self.r = 0
        self.left = None
        self.right = None
        return
    
class SegmentTreeDynamic2:
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
        node.val = node.left.val + node.right.val
        return
        
    
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


class SegmentTreeDynamic:
    def __init__(self, n):
        self.N = n
        self.root = Node()

    def update(self,  node, start, end, l, r, val, flag):
        # print('update', start, end, l, r, (start + end) >> 1, val)
        if l <= start and end <= r:
            if val != -1:
                node.val = val
            else:
                if flag == 1:
                    node.val = r - l + 1 - val
            node.add = (node.add + flag)%2

            # node.val += (end - start + 1) * val
            # node.add = flag
            return 
        
        mid = (start + end) >> 1
        self.pushDown(node, mid - start + 1, end - mid)
        if l <= mid: self.update(node.left, start, mid, l, r, val, flag)
        if r > mid: self.update(node.right, mid + 1, end, l, r, val, flag)
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
        node.val = node.left.val + node.right.val
        return
        
    
    def pushDown(self, node, leftNum, rightNum):
        if node.left == None: 
            node.left = Node()
            node.l = leftNum
        if node.right == None: 
            node.right = Node()
            node.r = rightNum
        if node.add == 0: return 
        # node.left.val += node.add
        # node.right.val += node.add
        # # 对区间进行「加减」的更新操作，下推懒惰标记时需要累加起来，不能直接覆盖
        node.left.add = (node.left.add + node.add)%2
        node.right.add = (node.right.add + node.add)%2
        node.add = 0



class Solution:
    # 26 / 77
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        tree = SegmentTreeDynamic(10**6)
        for i,v in enumerate(nums1):
            tree.update(tree.root, 0, tree.N, i , i , v, 0)
            
        s2 = sum(nums2)
        ans = []
        for t,l,r in queries:
            if t == 1:
                temp = tree.query(tree.root, 0, tree.N, l , r)
                tree.update(tree.root, 0, tree.N, l , r , -1, 1)
            elif t == 2:
                one = tree.query(tree.root, 0, tree.N, 0 , len(nums1))
                s2 = s2 + one * l
            elif t == 3:
                ans.append(s2)
        return ans
    
nums1 = [1,0,1]
nums2 = [0,0,0]
queries = [[1,1,1],[2,1,0],[3,0,0]]
nums1 = [1]
nums2 = [5]
queries = [[2,0,0],[3,0,0]]

nums1 = [0,0,0,0,1,0,0,0,1,1,0,1,0,1,1,1,0,0,0,0,1,1,1]
nums2 = [30,46,43,34,39,16,14,41,22,11,32,2,44,12,22,36,44,49,50,10,33,7,42]
queries = [[1,15,21],[3,0,0],[3,0,0],[2,21,0],[2,13,0],[3,0,0]]

# [679,679,1053]
sol = Solution()
print(sol.handleQuery(nums1, nums2, queries))
