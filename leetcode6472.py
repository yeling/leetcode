
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
    #MLE
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int: 
        #倒序，可用列数，可用行数
        col = n
        row = n
        visCol = [False] * n
        visRow = [False] * n
        ans = 0
        for i in range(len(queries)):
            #倒序
            t, index, v = queries[-1-i]
            if t == 0 and visRow[index] == False and col > 0:
                visRow[index] = True
                ans += col * v
                row -= 1
            elif t == 1 and visCol[index] == False and row > 0:
                visCol[index] = True
                ans += row * v
                col -= 1


        # print(ans)   
        return ans
    
n = 3
queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4],[1,0,1]]
# n = 3
# queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
sol = Solution()
print(sol.matrixSumQueries(n, queries))
