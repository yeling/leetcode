
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
    def maximumTripletValue(self, nums: List[int]) -> int:  
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j + 1, n):
                    ans = max(ans, (nums[i] - nums[j]) * nums[k])

        return ans
    
nums = [12,6,1,2,7]
nums = [1,10,3,4,19]
nums = [1,2,3]
sol = Solution()
print(sol.maximumTripletValue(nums))
