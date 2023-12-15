
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
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        out = [[] for _ in range(n)]
        for u,v in edges:
            out[v].append(u)
            out[u].append(v)
        # 返回节点和 (sum, cnt)
        def dfs(root, father):
            temp = values[root]
            cnt = 0
            if len(out[root]) == 0:
                if values[root]%k == 0:
                    return [0,1]
                else:
                    return [values[root], 0]
                
            for v in out[root]:
                if v != father:
                    s,c = dfs(v, root)
                    temp += s
                    cnt += c
                    # print(v, s, c)
            if temp%k == 0:
                temp = 0
                cnt += 1

            return [temp, cnt]
        sum, cnt = dfs(0, -1)
        return cnt
    
n = 7
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
values = [3,0,6,1,5,2,1]
k = 3
n = 5
edges = [[0,2],[1,2],[1,3],[2,4]]
values = [1,8,1,4,4]
k = 6
sol = Solution()
print(sol.maxKDivisibleComponents(n, edges, values, k))
