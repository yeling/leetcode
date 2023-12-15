
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
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:  
        stack = []
        ans = nums[-1]
        stack.append(())

        return
    
nums = [3,3,5,6]
sol = Solution()
print(sol.maxBalancedSubsequenceSum(nums))
