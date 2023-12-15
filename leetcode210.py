
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
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inList = [set() for _ in range(numCourses)]
        outList = [set() for _ in range(numCourses)]
        for a,b in prerequisites:
            outList[b].add(a)
            inList[a].add(b)
        ans = []
        stack = []
        for i,v in enumerate(inList):
            if len(v) == 0:
                stack.append(i)
                ans.append(i)
        # print(stack, outList, inList)
        while len(stack) > 0:
            cnt = len(stack)
            for i in range(cnt):
                for v in outList[stack[i]]:
                    inList[v].remove(stack[i])
                    if len(inList[v]) == 0:
                        stack.append(v)
                        ans.append(v)
            stack = stack[cnt:]
        if len(ans) == numCourses:
            return ans
        else:
            return []
    
numCourses = 2
prerequisites = [[1,0]]
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
sol = Solution()
print(sol.findOrder(numCourses ,prerequisites))

