
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
        pre = [0] * (n + 1)
        after = [0] * (n + 1)
        ans = 0
        for i in range(n):
            pre[i + 1] = max(pre[i], nums[i])
            after[n - 1 - i] = max(after[n - i], nums[n-1-i])
        # print(pre, after)
        for i in range(1, n - 1):
            ans = max(ans, (pre[i + 1] -  nums[i]) * after[i + 1])

        
        return ans
    
nums = [12,6,1,2,7]
nums = [1,10,3,4,19]
nums = [1,2,3]
nums = [10,13,6,2]
sol = Solution()
print(sol.maximumTripletValue(nums))
