
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
    # 116 / 204
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        g = [[] for _ in range(n+1)]
        for u,v in edges:
            g[v].append(u)
            g[u].append(v)
        stack = []
        #(index, possible)
        pos = [0] * (n + 1)
        vis = [False] * (n + 1)
        pos[1] = 1
        stack.append(1)
        depth = 0
    
        while depth < t and len(stack) > 0:
            cnt = len(stack)
            for i in range(cnt):
                flag = True
                for v in g[stack[i]]:
                    if vis[v] == True:
                        continue
                    flag = False
                    if stack[i] == 1:
                        pos[v] = pos[stack[i]] * (1/len(g[stack[i]]))
                    else:
                        pos[v] = pos[stack[i]] * (1/(len(g[stack[i]]) - 1))
                    stack.append(v)
                vis[stack[i]] = True
                if flag == False:
                    pos[stack[i]] = 0
            # print(pos)
            stack = stack[cnt:]
            depth += 1
        # print(pos)

        return pos[target]
    
n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 2
target = 4
n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 2
target = 7
sol = Solution()
print(sol.frogPosition(n, edges, t, target))
