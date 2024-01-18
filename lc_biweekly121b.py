
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
    def minOperations(self, nums: List[int], k: int) -> int: 
        curr = 0
        for v in nums:
            curr ^= v
        ans = 0
        for i in range(32):
            if (curr & (1 << i)) != (k & ( 1 << i)):
                ans += 1

        # print(v, k)   
        return ans
    
nums = [2,1,3,4]
k = 1
nums = [2,0,2,0]
k = 0
sol = Solution()
print(sol.minOperations(nums, k))
