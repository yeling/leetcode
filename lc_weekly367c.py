
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
from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

def min(a, b):
    if a[0] < b[0]:
        return a
    elif a[0] > b[0]:
        return b
    elif a[0] == b[0]:
        if a[1] < b[1]:
            return a
        else:
            return b

class Node:
    def __init__(self):
        self.val = (0,0)
        self.add = 0
        self.left = None
        self.right = None
        return

class SegmentTreeDynamic:
    def __init__(self):
        self.N = 10 ** 5
        self.root = Node()

    def update(self,  node, start, end, l, r, val):
        if l <= start and end <= r:
            node.val = (val, l)
            # 对区间进行「加减」的更新操作，需要 +=
            # node.val += (end - start + 1) * val
            # node.add += val
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
        ans = (INF,INF)
        self.pushDown(node, mid - start + 1, end - mid)
        if l <= mid: ans = min(ans, self.query(node.left, start, mid, l, r))
        if r > mid: ans = min(ans, self.query(node.right, mid + 1, end, l, r))
        #注意区间和的表示方法
   # ans = 0
   # self.pushDown(node, mid - start + 1, end - mid)
   # if l <= mid: ans += self.query(node.left, start, mid, l, r)
   # if r > mid: ans += self.query(node.right, mid + 1, end, l, r)
        return ans
        
    def pushUp(self, node):
        node.val = min(node.left.val , node.right.val)
        #注意区间和的上推
        #node.val = min(node.left.val , node.right.val)
    
    def pushDown(self, node, leftNum, rightNum):
        if node.left == None: node.left = Node()
        if node.right == None: node.right = Node()
        if node.add == 0: return 
        
        # node.left.val += node.add * leftNum
        # node.right.val += node.add * rightNum
        # # 对区间进行「加减」的更新操作，下推懒惰标记时需要累加起来，不能直接覆盖
        # node.left.add += node.add
        # node.right.add += node.add
        # node.add = 0

class Solution:
    #TLE 512 / 516

    def findIndices2(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]: 
        ma = SegmentTreeDynamic()
        mi = SegmentTreeDynamic()
        for i,v in enumerate(nums):
            ma.update(ma.root,  0, ma.N, i, i, -v)
            mi.update(mi.root,  0, mi.N, i, i, v)
            if i >= indexDifference:
                t1 = ma.query(ma.root, 0, ma.N, 0, max(0, i - indexDifference))
                if abs(v - (-t1[0])) >= valueDifference:
                    return [t1[1], i]
                
                t2 = mi.query(mi.root, 0, mi.N, 0, max(0, i - indexDifference))
                if abs(t2[0] - v) >= valueDifference:
                    return [t2[1], i]
                
        return [-1, -1]
    
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]: 
        # (index, value)
        ma = [0,0]
        mi = [0,INF]
        for i,v in enumerate(nums):
            if i >= indexDifference:
                if ma[1] <= nums[i - indexDifference]:
                    ma = [i - indexDifference, nums[i - indexDifference]]
                if mi[1] >= nums[i - indexDifference]:
                    mi = [i - indexDifference, nums[i - indexDifference]]
                if abs(ma[1] - v) >= valueDifference:
                    return [ma[0], i]
                if abs(mi[1] - v) >= valueDifference:
                    return [mi[0], i]

        return [-1, -1]
nums = [5,1,4,1]
indexDifference = 2
valueDifference = 4
# nums = [2,1]
# indexDifference = 0
# valueDifference = 0

# nums = [1,2,3]
# indexDifference = 2
# valueDifference = 4
sol = Solution()
print(sol.findIndices(nums, indexDifference, valueDifference))
