
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
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = 0
        for a,b,w in edges:
            n = max(n, a, b)
        n += 1
        ans = [0] * n
        grid = [[] for _ in range(n)]
        cnt = [0] * n
        for a,b,w in edges:
            grid[a].append((b,w))
            grid[b].append((a,w))

        def dfs(c, p, dis):
            for b,w in grid[c]:
                if b != p:
                    dfs(b, c, dis + w)
                    if (dis + w)%signalSpeed == 0:
                        cnt[b] += 1
                    cnt[c] += cnt[b]
                    

        for c in range(n):
            cnt = [0] * n
            dfs(c, -1, 0)
            tc = cnt[c]
            for b,w in grid[c]:
                ans[c] += cnt[b] * (tc - cnt[b])
                tc -= cnt[b]
            # print(cnt, ans)


        return ans
    
edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]]
signalSpeed = 1

# edges = [[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]]
# signalSpeed = 3
sol = Solution()
print(sol.countPairsOfConnectableServers(edges, signalSpeed))
