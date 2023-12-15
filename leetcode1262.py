
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
    def maxSumDivThree(self, nums: List[int]) -> int:   
        #0,1,2
        cache = [[] for _ in range(3)]

        s = 0
        ans = 0
        for v in nums:
            s += v
            cache[v%3].append(v) 
        for i in range(3):
            cache[i].sort()
        if s%3 == 1:
            if len(cache[1]) > 0:
                ans = max(ans, s - cache[1][0])
            if len(cache[2]) > 1:
                ans = max(ans, s - cache[2][0] - cache[2][1])
        elif s%3 == 2:
            if len(cache[2]) > 0:
                ans = max(ans, s - cache[2][0])
            if len(cache[1]) > 1:
                ans = max(ans, s - cache[1][0] - cache[1][1])
        else:
            ans = s
        return ans
    
nums = [3,6,5,8]
sol = Solution()
print(sol.maxSumDivThree(nums))
