
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

class Solution:
    #TLE 38 / 40 
    def numSubmatrixSumTarget2(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        pre = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                pre[i+1][j+1] = pre[i][j + 1] + pre[i + 1][j] + matrix[i][j] - pre[i][j]
        ans = 0
        for x1 in range(n):
            for y1 in range(m):
                for x2 in range(x1,n):
                    for y2 in range(y1,m):
                        temp = pre[x2 + 1][y2 + 1] - pre[x1][y2 + 1] - pre[x2 + 1][y1] + pre[x1][y1]
                        if temp == target:
                            ans += 1

        return ans
    
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        pre = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                pre[i+1][j+1] = pre[i][j + 1] + pre[i + 1][j] + matrix[i][j] - pre[i][j]
        ans = 0
        for top in range(n):
            for bot in range(top,n):
                cache = defaultdict(int)
                for r in range(m):
                    temp = pre[bot + 1][r + 1] - pre[top][r + 1]
                    if temp == target:
                        ans += 1
                    if cache[temp - target] != 0:
                        ans += cache[temp - target]
                    cache[temp] += 1
                    # print(top, bot, ans)
        
        return ans
    
matrix = [[0,1,0],[1,1,1],[0,1,0]]
target = 0
matrix = [[1,-1],[-1,1]]
target = 0

sol = Solution()
print(sol.numSubmatrixSumTarget(matrix, target))
