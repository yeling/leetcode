
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
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        ans = [[0]*n for _ in range(m)]
        #贪心，每个元素尽可能的大
        currRow = [0] * m
        currCol = [0] * n
        for i in range(m):
            for j in range(n):
                curr = min(rowSum[i] - currRow[i], colSum[j] - currCol[j])
                ans[i][j] = curr
                currRow[i] += curr
                currCol[j] += curr
        # print(ans)

        return ans
    
rowSum = [3,8]
colSum = [4,7]
rowSum = [5,7,10]
colSum = [8,6,8]
rowSum = [14,9]
colSum = [6,9,8]
sol = Solution()
print(sol.restoreMatrix(rowSum, colSum))
