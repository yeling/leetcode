
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

# Python模版
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
    # 1017 / 1022 个通过测试用例
    # 718 / 1022 个通过测试用例
    # 线段树
    def checkArray2(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        
        tree = SegmentTreeDynamic()
        n = len(nums)
        for i,v in enumerate(nums):
            diff = tree.query(tree.root, 0, tree.N, i, i)
            temp = v + diff
            # print(v, diff, temp)
            if temp < 0:
                return False
            if temp > 0:
                tree.update(tree.root, 0, tree.N, i, i + k - 1 , -temp)
            if i + k > n and temp != 0:
                return False
        return True
    
    #差分数组
    def checkArray(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        n = len(nums)
        diff = [0]*(n + 1)
        preSum = 0
        for i,v in enumerate(nums):
            # print(diff)
            preSum += diff[i]
            v += preSum
            if v == 0:
                continue
            elif v < 0:
                return False
            #v > 0
            if i + k > n:
                return False
            preSum -= v
            diff[i + k] += v

        return True
        
nums = [2,2,3,1,1,0]
k = 3
nums = [1,3,1,1]
k = 2

# nums = [0,45,82,98,99]
# k = 4

# nums = [60,72,87,89,63,52,64,62,31,37,57,83,98,94,92,77,94,91,87,100,91,91,50,26]
# k = 4

sol = Solution()
print(sol.checkArray2(nums, k))
print(sol.checkArray(nums, k))
