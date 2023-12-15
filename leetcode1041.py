
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
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        cache = set()
        pos = [0,0]
        dir = 0
        for i in range(4):
            for v in instructions:
                cache.add(tuple(pos))
                if v == 'G':
                    pos[0] += dirs[dir][0]
                    pos[1] += dirs[dir][1]
                elif v == 'L':
                    dir -= 1
                    dir = (dir + 4)%4
                elif v == 'R':
                    dir += 1
                    dir = (dir + 4)%4

        cnt = 0
        for v in instructions:
            if tuple(pos) in cache:
                cnt += 1 
            if v == 'G':
                pos[0] += dirs[dir][0]
                pos[1] += dirs[dir][1]
            elif v == 'L':
                dir -= 1
                dir = (dir + 4)%4
            elif v == 'R':
                dir += 1
                dir = (dir + 4)%4
        print(cache, cnt)

        return cnt == len(instructions)
    
instructions = "GLR"
sol = Solution()
print(sol.isRobotBounded(instructions))
