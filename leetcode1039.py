
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
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        @cache
        def dfs(i,j): 
            # print(i, j)
            if j - i == 1:
                return 0
            if j - i == 2:
                return values[i] * values[j] * values[i + 1]
            ans = INF
            for k in range(i+1,j):
                ans = min(ans, dfs(i,k) + dfs(k,j) + values[i] * values[j] * values[k])
            return ans
            
        return dfs(0, n - 1)
    
values = [1,3,1,4,1,5]
# values = [3,7,4,1]
sol = Solution()
print(sol.minScoreTriangulation(values))
