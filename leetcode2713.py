
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

class Solution:
    # 552 / 564 个通过测试用例
    def maxIncreasingCells2(self, mat: List[List[int]]) -> int:    
        m = len(mat)
        n = len(mat[0])
        inDegree = [[0] * n for _ in range(m)]
        outDegree = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                inDegree[i][j] = set()
                outDegree[i][j] = set()
        stack = []
        for i in range(m):
            for j in range(n):
                for c in range(m):
                    if mat[i][j] < mat[c][j]:
                        inDegree[c][j].add((i,j))
                        outDegree[i][j].add((c,j))
                for r in range(n):
                    if mat[i][j] < mat[i][r]:
                        inDegree[i][r].add((i,j))
                        outDegree[i][j].add((i,r))
        for i in range(m):
            for j in range(n):
                if len(inDegree[i][j]) == 0:
                    stack.append((i,j))
        depth = 0
        while len(stack) > 0:
            depth += 1
            next = []
            for i,j in stack:
                for vi,vj in outDegree[i][j]:
                    inDegree[vi][vj].remove((i,j))
                    if len(inDegree[vi][vj]) == 0:
                        next.append((vi,vj))
            stack = next
            # print(stack, depth)
        return depth
    
    # 558 / 564 个通过测试用例 OUT OF MEMORY
    def maxIncreasingCells3(self, mat: List[List[int]]) -> int:    
        m = len(mat)
        n = len(mat[0])
        inDegree = [[0] * n for _ in range(m)]
        outDegree = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                outDegree[i][j] = set()
        stack = []
        for i in range(m):
            for j in range(n):
                for c in range(m):
                    if mat[i][j] < mat[c][j]:
                        inDegree[c][j] += 1
                        outDegree[i][j].add((c,j))
                for r in range(n):
                    if mat[i][j] < mat[i][r]:
                        inDegree[i][r] += 1
                        outDegree[i][j].add((i,r))
        for i in range(m):
            for j in range(n):
                if inDegree[i][j] == 0:
                    stack.append((i,j))
        depth = 0
        while len(stack) > 0:
            depth += 1
            next = []
            for i,j in stack:
                for vi,vj in outDegree[i][j]:
                    inDegree[vi][vj] -= 1
                    if inDegree[vi][vj] == 0:
                        next.append((vi,vj))
            stack = next
            # print(stack, depth)
        return depth
    # 558 / 564 个通过测试用例 TLE
    # 558 / 564 个通过测试用例
    def maxIncreasingCells4(self, mat: List[List[int]]) -> int:    
        m = len(mat)
        n = len(mat[0])
        inDegree = [[0] * n for _ in range(m)]
        vis = [[False] * n for _ in range(m)]
        stack = []
        cols = [[0]*m for _ in range(n)]
        for i in range(m):
            row = mat[i][:]
            row.sort()
            for j in range(n):
                pos = bisect_right(row, mat[i][j] - 1)
                inDegree[i][j] += pos
        for i in range(m):
            for j in range(n):
                cols[j][i] = mat[i][j]
        for i in range(n):
            cols[i].sort()
            for j in range(m):
                pos = bisect_right(cols[i], mat[j][i] - 1)
                inDegree[j][i] += pos
        
        for i in range(m):
            for j in range(n):
                if inDegree[i][j] == 0:
                    stack.append((i,j))
        depth = 0
        # print(inDegree)
        while len(stack) > 0:
            depth += 1
            next = []
            for i,j in stack:                
                vis[i][j] = True
                for c in range(m):
                    if mat[i][j] < mat[c][j] and vis[c][j] == False:
                        inDegree[c][j] -= 1
                        if inDegree[c][j] == 0 :
                            next.append((c,j))
                            vis[c][j] = True
                for r in range(n):
                    if mat[i][j] < mat[i][r] and vis[i][r] == False:
                        inDegree[i][r] -= 1
                        if inDegree[i][r] == 0 :
                            next.append((i,r))
                            vis[i][r] = True
            stack = next
            # print(stack, depth)
        return depth
    
    # 558 / 564 个通过测试用例
    # dp 存储每行，每列的最大值
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:    
        m = len(mat)
        n = len(mat[0])
        g = defaultdict(list)
        for i in range(m):
            for j in range(n):
                g[mat[i][j]].append((i,j))

        allKeys = list(g.keys())
        allKeys.sort()
        rowMax = [0] * m
        colMax = [0] * n
        ans = 0
        for k in allKeys:
            mx = []
            for i,j in g[k]:
                mx.append(max(rowMax[i], colMax[j]) + 1)
            
            for i in range(len(mx)):
                rowMax[g[k][i][0]] = max(rowMax[g[k][i][0]], mx[i])
                colMax[g[k][i][1]] = max(colMax[g[k][i][1]], mx[i])
                ans = max(ans, mx[i])
        
        return ans



    
    
mat = [[3,1,6],[-9,5,7]]
# mat = [[1,1],[1,1]]
mat = [[2,-4,2,-2,6]]
sol = Solution()
print(sol.maxIncreasingCells2(mat))
print(sol.maxIncreasingCells(mat))
