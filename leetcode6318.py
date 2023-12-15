
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
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        state = [0] * 2002
        sTask = [list()] * 2002
        oneTask = []
        leftTask = []
        for s,e,d in tasks:
            if e - s + 1 == d:
                oneTask.append([s,e,d])
                for i in range(s, e + 1):
                    state[i] = 1
            else:
                for i in range(s, e + 1):
                    sTask[i].append([s,e,d])
        #oneTask
        
                    
                

        return
    
tasks = [[1,3,2],[2,5,3],[5,6,2]]
sol = Solution()
print(sol.findMinimumTime(tasks))
