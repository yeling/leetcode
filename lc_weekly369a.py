
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
    def findKOr(self, nums: List[int], k: int) -> int:  
        cache = [0]*32
        for v in nums:
            for i in range(32):
                if v & (1 << i):
                    cache[i] += 1
        ans = 0
        for i in range(32):
            if cache[i] >= k:
                ans += (1 << i)

        # print(cache)  
        return ans
    
nums = [7,12,9,8,9,15]
k = 4
nums = [2,12,1,11,4,5]
k = 6
nums = [10,8,5,9,11,6,8]
k = 1
sol = Solution()
print(sol.findKOr(nums,k))
