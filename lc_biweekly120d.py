
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
    # 217 / 614 个通过测试用例
    # AC
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]: 
        n = len(cost)  
        coins = [0] * n
        g = [[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(u,f):
            nonlocal coins
            temp = [cost[u]]
            for v in g[u]:
                if v != f:
                    temp += dfs(v, u)
            temp.sort()
            if len(temp) < 3:
                coins[u] = 1
                return temp
            else:
                ans = 0
                ans = max(ans, temp[-1] * temp[-2] * temp[-3])
                ans = max(ans, temp[0] * temp[1] * temp[-1])
                coins[u] = ans
                lt = len(temp)
                if lt <= 5:
                    return temp[:]
                else: 
                    return [temp[0], temp[1], temp[-3], temp[-2], temp[-1]]
            return
        
        dfs(0, -1) 
        return coins
    
# edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]]
# cost = [1,4,2,3,5,7,8,-4,2]
edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]
cost = [1,2,3,4,5,6]
edges = [[0,2],[0,6],[1,4],[3,5],[7,6],[3,6],[1,8],[3,1],[9,3]]
cost = [63,13,-6,20,56,-14,61,25,-99,54]
# [215208,0,1,77616,1,1,184464,1,1,1]

sol = Solution()
print(sol.placedCoins(edges, cost))
