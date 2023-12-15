
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
    def minimumPossibleSum(self, n: int, target: int) -> int:  
        ans = 0
        dp = defaultdict(int)
        i = 1
        while len(dp) < n:
            if target - i not in dp:
                dp[i] = 1
                ans += i
            i += 1
        
        return ans
    
n = 3
target = 3
n = 1
target = 1
sol = Solution()
print(sol.minimumPossibleSum(n, target))
