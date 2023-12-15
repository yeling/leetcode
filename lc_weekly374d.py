
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
    def numberOfSequence(self, n: int, sick: List[int]) -> int:  
        if len(sick) == n:
            return 0
        ans = 1
        for i in range(len(sick)):
            if i == 0: 
                if sick[i] > 0:
                    ans *= sick[0]
            if i == len(sick) - 1:
                if sick[-1] != n - 1:
                    ans *= n - 1 - sick[-1]
            if i > 0:
                le = sick[i] - sick[i - 1] - 2
                # print(le)
                if le > 0:
                    ans *= (1 << le)
                
            ans %= MOD
        return ans
    
n = 5
sick = [0,4]
n = 4
sick = [1]
# n = 2
# sick = [0]
sol = Solution()
print(sol.numberOfSequence(n, sick))
