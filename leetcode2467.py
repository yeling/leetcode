
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
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        g = defaultdict(list)
        n = len(amount)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        bobTime = [n] * n
        def dfsBos(u, fa, time):
            if u == 0:
                bobTime[0] = time
                return True
            for v in g[u]:
                if v != fa and dfsBos(v, u, time + 1):
                    bobTime[u] = time
                    return True
            return False
        dfsBos(bob, -1, 0)
        # print(bobTime,g )
        g[0].append(-1) 
        self.ans = -INF

        def dfsAlice(u, fa, atime, total):
            # print(u, atime, total)
            if atime < bobTime[u]:
                total += amount[u]
            elif atime == bobTime[u]:
                total += amount[u]//2
            if len(g[u]) == 1:
                self.ans = max(self.ans, total)
            for v in g[u]:
                if v != fa:
                    dfsAlice(v, u, atime + 1, total)

        dfsAlice(0, -1, 0, 0)

        return self.ans
        
    
edges = [[0,1],[1,2],[1,3],[3,4]]
bob = 3
amount = [-2,4,2,-4,6]

edges = [[0,1],[1,2],[2,3]]
bob = 3
amount = [-5644,-6018,1188,-8502]
sol = Solution()
print(sol.mostProfitablePath(edges, bob, amount))
