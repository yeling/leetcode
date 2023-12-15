
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
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            ans += mat[i][i] + mat[n-1-i][i]
        if n%2 == 1:
            ans -= mat[i//2][i//2]

        return ans
    
mat = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
print(sol.diagonalSum(mat))
