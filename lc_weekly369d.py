
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
    # TLE 540 / 542
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        g = [[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        power = [[0] * 32 for _ in range(n)]
        for i in range(n):
            for j in range(32):
                if j == 0:
                    power[i][j] = coins[i]
                else:
                    power[i][j] = power[i][j - 1]//2
        
        @cache
        def calc(v, p):
            temp = v
            for i in range(p):
                temp = temp//2
                if temp == 0:
                    break
            return temp

        @cache
        def dfs(c, p, pow):
            # print(c, p)
            if pow >= 32:
                return 0
            ret = 0
            for v in g[c]:
                if v != p:
                    # nv = calc(coins[v], pow)
                    if pow >= 32:
                        nv = 0
                    else:
                        nv = power[v][pow]
                    m1 = dfs(v, c, pow) + nv - k
                    m2 = dfs(v, c, pow + 1) + nv//2
                    curr = max(m1, m2)
                    ret += curr
                    # print(m1, m2, curr, ret)
            return ret
        # ans = dfs(0, -1, 0)
        ans = max(dfs(0, -1, 0) + coins[0] - k, dfs(0, -1, 1) + coins[0]//2)
        return ans
    
edges = [[0,1],[0,2]]
coins = [8,4,4]
k = 0
edges = [[0,1],[1,2],[2,3]]
coins = [10,10,3,3]
k = 5
sol = Solution()
print(sol.maximumPoints(edges, coins, k))
