
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
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        curr = [0,0]
        dir = 0
        cache = set((x,y) for x,y in obstacles)
        ans = 0
        for c in commands:
            if c == -1:
                dir = (dir + 1)%4
            elif c == -2:
                dir = (dir + 4 - 1)%4
            else:
                for i in range(1,c + 1):
                    if (curr[0] + dirs[dir][0], curr[1] + dirs[dir][1]) in cache:
                        break
                    else:
                        curr = [curr[0] + dirs[dir][0], curr[1] + dirs[dir][1]]
                        ans = max(ans ,curr[0] * curr[0] + curr[1] * curr[1])
            
        # print(cache)
        return ans
    
commands = [4,-1,4,-2,4]
obstacles = [[2,4]]

commands = [4,-1,3]
obstacles = []

sol = Solution()
print(sol.robotSim(commands, obstacles))
