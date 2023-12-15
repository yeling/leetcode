
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
    def minPushBox(self, grid: List[List[str]]) -> int:
        # S B . # T
        m = len(grid)
        n = len(grid[0])
        #状态 (si,sj,bi,bj,v) bfs
        stack = deque()
        s,b,t = 0,0,0
        ans = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    s = (i,j)
                elif grid[i][j] == 'T':
                    t = (i,j)
                elif grid[i][j] == 'B':
                    b = (i,j)
        vis = defaultdict(bool)
        curr = (s[0], s[1], b[0], b[1], 0)
        stack.append(curr)
        # vis[(s[0], s[1], b[0], b[1])] = True
        dirs = [[0,1],[0,-1],[-1,0],[1,0]]
        while len(stack) > 0:
            # print(stack)
            curr = stack.popleft()
            for dv in dirs:
                dx = curr[0] + dv[0]
                dy = curr[1] + dv[1]
                # print(curr, dx, dy, (dx, dy, curr[2], curr[3]), vis[(dx, dy, curr[2], curr[3])])
                if 0 <= dx < m and  0 <= dy < n and grid[dx][dy] != '#' and vis[(dx, dy, curr[2], curr[3])] == False:
                    #箱子能推动
                    if dx == curr[2] and dy == curr[3]:
                        bx = curr[2] + dv[0]
                        by = curr[3] + dv[1]
                        
                        if 0 <= bx < m and 0 <= by < n:
                            if grid[bx][by] == 'T':
                                ans = curr[4] + 1
                                return ans
                            elif grid[bx][by] != '#':
                                # 距离+1，加到尾部
                                next = (dx, dy, bx, by, curr[4] + 1)
                                stack.append(next)
                    else:
                        # 距离不变，加到头上
                        next = (dx, dy, curr[2], curr[3], curr[4])
                        stack.appendleft(next)
            # print((curr[0], curr[1], curr[2], curr[3]))
            vis[(curr[0], curr[1], curr[2], curr[3])] = True
        return ans
 
grid = [["#","#","#","#","#","#"],
        ["#","T",".",".","#","#"],
        ["#",".","#",".","B","#"],
        ["#",".",".",".",".","#"],
        ["#",".",".",".","S","#"],
        ["#","#","#","#","#","#"]]
sol = Solution()
print(sol.minPushBox(grid))
