
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

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        ans = [[0] * n for _ in range(m)]
        k = k%n
        for i in range(m):
            for j in range(n):
                if i%2 == 0:
                    ans[i][j] = mat[i][(j + k)%n]
                else:
                    ans[i][j] = mat[i][(j + n - k)%n]
        for i in range(m):
            for j in range(n):
                if ans[i][j] != mat[i][j]:
                    return False

        return True
    
mat = [[1,2,1,2],[5,5,5,5],[6,3,6,4]]
k = 2
sol = Solution()
print(sol.areSimilar(mat, 2))
