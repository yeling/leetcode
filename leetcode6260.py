
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
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        k = len(queries)
        ans = [0] * k
        queries = list(zip(queries,range(k)))
        queries.sort()
        stack = deque()
        border = deque()
        vis = [[False] * n for _ in range(m)]
        border.append((0,0))
        last = 0
        dirs = [[0,1],[0,-1],[-1,0],[1,0]]
        # print(queries)
        for v in queries:
            stack = border.copy()
            border.clear()
            # print(v ,stack)
            while len(stack) > 0:
                curr = stack.popleft()
                if grid[curr[0]][curr[1]] < v[0]:
                    # print(v , curr)
                    last += 1
                    vis[curr[0]][curr[1]]  = True
                    for dv in dirs:
                        dx = curr[0] + dv[0]
                        dy = curr[1] + dv[1]
                        if 0 <= dx < m and  0 <= dy < n and vis[dx][dy] == False:
                            stack.append((dx,dy))
                            vis[dx][dy] = True
                else:
                    border.append(curr)

            ans[v[1]] = last
        return ans

grid = [[1,2,3],[2,5,7],[3,5,1]]
queries = [5,6,2]
# grid = [[5,2,1],[1,1,2]]
# queries = [3]

sol = Solution()
print(sol.maxPoints(grid, queries))
