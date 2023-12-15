
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        ans = [0,0]
        for i in range(m):
            cnt = mat[i].count(1)
            if ans[1] < cnt:
                ans[1] = cnt
                ans[0] = i


        return ans
    
mat = [[0,0,0],[0,1,1]]
mat = [[0,1],[1,0]]
mat = [[0,0],[1,1],[0,0]]
sol = Solution()
print(sol.rowAndMaximumOnes(mat))
