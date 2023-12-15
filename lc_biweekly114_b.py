
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
    def minOperations(self, nums: List[int]) -> int:  
        cache = defaultdict(int)
        for v in nums:
            cache[v] += 1
        # print(cache)
        ans = 0
        for k in cache:
            if cache[k] == 1:
                return -1
            if cache[k]%3 != 0:
                ans +=  cache[k]//3 + 1
            else:
                ans += cache[k]//3
            
        return ans
    
nums = [2,3,3,2,2,4,2,3,4]
nums = [2,1,2,2,3,3]
sol = Solution()
print(sol.minOperations(nums))
