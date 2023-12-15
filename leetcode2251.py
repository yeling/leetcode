
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
        if l <= start and end <= r:
            # node.val += val
            # 对区间进行「加减」的更新操作，需要 +=
            node.val += (end - start + 1) * val
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
        
        node.left.val += node.add
        node.right.val += node.add
        # # 对区间进行「加减」的更新操作，下推懒惰标记时需要累加起来，不能直接覆盖
        node.left.add += node.add
        node.right.add += node.add
        node.add = 0
    

class Solution:
    # 46 / 52 TLE
    def fullBloomFlowers2(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        #区间操作，差分数组，求出前缀和数组，数据范围太大，
        # 改用线段树, 卡常数
        ma = 0
        for s,e in flowers:
            if e > ma:
                ma = e
        tree = SegmentTreeDynamic(ma + 1)
        for s,e in flowers:
            tree.update(tree.root, 0, tree.N, s, e, 1)
        ans = []
        for v in people:
            if v > ma:
                ans.append(0)
            else:
                ans.append(tree.query(tree.root, 0, tree.N, v, v))
        return ans
    
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        #区间操作，差分数组，求出前缀和数组，数据范围太大，
        #线段树, 卡常数
        ma = 0
        pre = defaultdict(int)
        for s,e in flowers:
            pre[s] += 1
            pre[e + 1] -= 1
        # print(pre)
        ks = list(pre.keys())
        ks.sort()
        preSum = [0] * (len(ks) + 1)
        for i,k in enumerate(ks):
            preSum[i + 1] = preSum[i] + pre[k]

        
        ans = []
        for v in people:
            pos = bisect_right(ks, v)
            ans.append(preSum[pos])
        return ans

# print(log(10 ** 9, 2))   
flowers = [[1,6],[3,7],[9,12],[4,13]]
people = [2,3,7,11]
flowers = [[1,10],[3,3]]
people = [3,3,2]
sol = Solution()
print(sol.fullBloomFlowers(flowers, people))
