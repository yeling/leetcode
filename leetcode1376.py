
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = [[] for _ in range(n)] 
        for i,v in enumerate(manager):
            if v != -1:
                g[v].append(i)
        # print(g)
        self.ans = 0
        def dfs(curr, time):
            if len(g[curr]) > 0:
                self.ans = max(self.ans, time)
            for v in g[curr]:
                dfs(v, time + informTime[v])
            return
        dfs(headID, informTime[headID])
        return self.ans
    
n = 6
headID = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,5,6,0]
sol = Solution()
print(sol.numOfMinutes(n, headID, manager, informTime))
