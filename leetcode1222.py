
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
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        cache = set([(x,y) for x,y in queens])
        # print(cache)
        x,y = king
        dirs = [[-1,-1],[-1,0],[-1,1],[0,1],[0,-1],[1,-1],[1,0],[1,1]]
        for d in dirs:
            for i in range(8):
                if (x + d[0] * i, y + d[1] * i) in cache:
                    ans.append([x + d[0] * i, y + d[1] * i])
                    break
        return ans
    
queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
king = [0,0]
queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]
king = [3,3]
sol = Solution()
print(sol.queensAttacktheKing(queens, king))
