
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
    def maxIncreasingGroups2(self, usageLimits: List[int]) -> int:
        stack = []
        n = len(usageLimits)
        for v in usageLimits:
            heappush(stack, -v)
        ans = 0
        for i in range(1,n+1):
            temp = []
            j = 0
            while j < i and len(stack) > 0:
                temp.append(-heappop(stack))
                j += 1
            # print(temp)
            if j == i:
                for v in temp:
                    if v > 1:
                        heappush(stack, -(v - 1))
                continue
            else:
                ans = i - 1
                break
            
        return ans
    
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        stack = []
        n = len(usageLimits)
        for v in usageLimits:
            heappush(stack, -v)
        ans = 0
        for i in range(1,n+1):
            temp = []
            j = 0
            while j < i and len(stack) > 0:
                temp.append(-heappop(stack))
                j += 1
            # print(temp)
            if j == i:
                for v in temp:
                    if v > 1:
                        heappush(stack, -(v - 1))
                continue
            else:
                ans = i - 1
                break
            
        return ans
    
usageLimits = [1,2,2,3]
# usageLimits = [2,1,2]
# usageLimits = [1,1]
sol = Solution()
print(sol.maxIncreasingGroups(usageLimits))
