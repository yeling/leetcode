
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
        nums.sort()
        ans = 0
        for v in nums:
            if v < k:
                ans += 1
            else:
                break


        return ans
    
nums = [2,11,10,1,3]
k = 10
sol = Solution()
print(sol.minOperations(nums, k))
