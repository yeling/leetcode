
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
        self.val = -INF
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
            node.val = val
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
        ans = -INF
        self.pushDown(node, mid - start + 1, end - mid)
        if l <= mid: ans = max(ans, self.query(node.left, start, mid, l, r))
        if r > mid: ans = max(ans, self.query(node.right, mid + 1, end, l, r))
        #注意区间和的表示方法
        # ans = 0
        # self.pushDown(node, mid - start + 1, end - mid)
        # if l <= mid: ans += self.query(node.left, start, mid, l, r)
        # if r > mid: ans += self.query(node.right, mid + 1, end, l, r)
        return ans
        
    def pushUp(self, node):
        node.val = max(node.left.val , node.right.val)
    
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
    # 63 / 66  TLE
    def findMaxValueOfEquation2(self, points: List[List[int]], k: int) -> int:
        n = points[-1][0] + 10 ** 8 
        tree = SegmentTreeDynamic(n)
        for x,y in points:
            tree.update(tree.root, 0, n, x + 10 ** 8, x + 10 ** 8, x + y)
        ans = -INF
        for x,y in points:
            temp = tree.query(tree.root, 0, n, x + 10 ** 8 + 1, min(n,x + 10 ** 8 + k))
            ans = max(ans, temp + y - x)

        return ans
    # 63 / 66  TLE 线段树
    def findMaxValueOfEquation2(self, points: List[List[int]], k: int) -> int:
        n = points[-1][0] - points[0][0]
        tree = SegmentTreeDynamic(n)
        for x,y in points:
            tree.update(tree.root, 0, n, x - points[0][0], x - points[0][0], x + y)
        ans = -INF
        for x,y in points:
            temp = tree.query(tree.root, 0, n, x -  points[0][0] + 1, min(n,x - points[0][0] + k))
            ans = max(ans, temp + y - x)

        return ans
    
    # 优先队列
    # 62 / 66 
    # AC
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ans = -INF
        l = 0
        r = 1
        n = len(points)
        # [(x + y, x)]
        stack = []
        # curr = heappop(stack)
        # heappush(stack, (dis[v[0]], v[0]))
        while l < n - 1:
            # 入队
            while r < n and points[r][0] - points[l][0] <= k:
                heappush(stack, (-(points[r][0] + points[r][1]), points[r][0]))
                r += 1
            if len(stack) == 0:
                l += 1
                continue
            temp = heappop(stack)
            while temp[1] <= points[l][0] and len(stack) > 0:
                temp = heappop(stack)
            if temp[1] > points[l][0]:
                ans = max(ans, points[l][1] - points[l][0] - temp[0])
                heappush(stack,temp)
            # print(l, ans, stack)
            l += 1
            # print(temp)
        return ans
    
points = [[1,3],[2,0],[5,10],[6,-10]]
k = 1

# points = [[0,0],[3,0],[9,2]]
# k = 3

# points = [[-17,13],[2,1],[8,-5],[18,-20]]
# k = 26

# points = [[-19,9],[-15,-19],[-5,-8]]
# k = 10


points = [[-99999220,15689984],[-99997843,69565311],[-99994192,9882747],[-99991675,78590288],[-99990325,82187552],[-99987425,-79590489],[-99987389,-21740205],[-99986308,37842445]]
points = [[-99999220,15689984],[-99997843,69565311],[-99994192,9882747],[-99991675,78590288]]
k = 200000000
 
points = [[-17,5],[-10,-8],[-5,-13],[-2,7],[8,-14]]
k = 4

points = [[-18,7],[-15,16],[5,-4],[10,-9],[15,16]]
k = 18

sol = Solution()
print(sol.findMaxValueOfEquation2(points, k))

print(sol.findMaxValueOfEquation(points, k))

