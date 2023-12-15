
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
    def maxDistToClosest(self, seats: List[int]) -> int:   
        n = len(seats)
        pre = [-1]*(n + 1)
        after = [-1]*(n + 2)
        for i,v in enumerate(seats):
            if v == 1:
                pre[i + 1] = i
            else:
                pre[i + 1] = pre[i]

        for i in range(n - 1, -1, -1):
            if seats[i] == 1:
                after[i + 1] = i
            else:
                after[i + 1] = after[i + 2]
        #
        ans = 0
        # print(pre, after)
        for i in range(n):
            if seats[i] == 1:
                continue
            if pre[i + 1] == -1:
                temp = after[i + 1] - i 
            elif after[i + 1] == -1:
                temp = i - pre[i + 1]
            else:
                temp = min(i - pre[i + 1], after[i + 1] - i)
            # print(i, temp)
            ans = max(ans, temp)

        return ans
    
seats = [1,0,0,0,1,0,1]
seats = [1,0,0,0]
sol = Solution()
print(sol.maxDistToClosest(seats))
