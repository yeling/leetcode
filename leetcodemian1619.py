
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

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        #bfs
        n = len(land)
        m = len(land[0])
        vis = [[False]*m for _ in range(n)]
        ans = []
        dirs = [[1,0], [-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        for i in range(n):
            for j in range(m):
                if land[i][j] == 0 and vis[i][j] == False:
                    currSize = 0
                    stack = [(i,j)]
                    vis[i][j] = True
                    while len(stack) > 0:
                        curr = stack.pop()
                        currSize += 1
                        for k in dirs:
                            dx = curr[0] + k[0]
                            dy = curr[1] + k[1]
                            if 0 <= dx < n and  0 <= dy < m and vis[dx][dy] == False and land[dx][dy] == 0:
                                vis[dx][dy] = True
                                stack.append((dx,dy))
                    ans.append(currSize)
        return ans
    

sol = Solution()
print()
