
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
    def hasTrailingZeros(self, nums: List[int]) -> bool: 
        even = 0
        for v in nums:
            if v%2 == 0:
                even += 1   
        return even > 1
    
nums = [1,2,3,9,5]
sol = Solution()
print(sol.hasTrailingZeros(nums))
