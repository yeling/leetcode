
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
    def maxSpending(self, values: List[List[int]]) -> int:  
        all = []
        m = len(values)
        n = len(values[0])
        for i in range(m):
            for j in range(n):
                all.append(values[i][j])
        
        all.sort()
        ans = 0
        for i in range(1, m*n + 1):
            ans += all[i - 1] * i
            
        # print(all)  
        return ans
    
values = [[8,5,2],[6,4,1],[9,7,3]]
values = [[10,8,6,4,2],[9,7,5,3,2]]
sol = Solution()

print(sol.maxSpending(values))
