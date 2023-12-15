
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
    def __init__(self):
        self.N = 10 ** 9
        self.root = Node()

    def update(self,  node, start, end, l, r, val):
        if l <= start and end <= r:
            node.val = val
            # node.val += (end - start + 1) * val
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
        ans = INF
        self.pushDown(node, mid - start + 1, end - mid)
        if l <= mid: ans = min(ans, self.query(node.left, start, mid, l, r))
        if r > mid: ans = min(ans, self.query(node.right, mid + 1, end, l, r))
        return ans
        
    def pushUp(self, node):
        node.val = min(node.left.val , node.right.val)
    
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
   
    #13 / 30 个通过测试用例
    #TLE
    def rangeAddQueries3(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0]*n for _ in range(n)]
        for v in queries:
            s = v[:2]
            e = v[2:]
            for i in range(s[0],e[0]+1):
                for j in range(s[1],e[1] + 1):
                    mat[i][j] += 1
        return mat
    #AC
    def rangeAddQueries2(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0]*n for _ in range(n)]
        tree = SegmentTreeDynamic()
        for v in queries:
            s = v[:2]
            e = v[2:]
            tree.update(tree.root, 0, n ** 2, s[0]*n + s[1], e[0]*n + e[1],1)
        for i in range(n*n):
            mat[i//n][i%n] = tree.query(tree.root, 0,n ** 2, i,i)
        return mat

    #差分数组，拆分数组的前缀和，刚好是每个元素的值
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0]*(n + 1) for _ in range(n + 1)]
        diff = [[0]*(n + 1) for _ in range(n + 1)]
        for v in queries:
            s = v[:2]
            e = v[2:]
            diff[s[0]][s[1]] += 1
            diff[e[0] + 1][e[1] + 1] += 1
            diff[s[0]][e[1] + 1] -= 1
            diff[e[0] + 1][s[1]] -= 1
        # print(diff)
        for i in range(1,n + 1):
            for j in range(1,n + 1):
                mat[i][j] = diff[i - 1][j - 1] + mat[i-1][j] + mat[i][j - 1] - mat[i-1][j-1]
        del mat[0]
        for v in mat:
            del v[0]
        return mat

n = 3
# queries = [[1,1,2,2],[0,0,1,1]]
queries = [[1,1,2,2]]

# n = 2
# queries = [[0,0,1,1]]

sol = Solution()
print(sol.rangeAddQueries3(n,queries))
print(sol.rangeAddQueries(n,queries))
