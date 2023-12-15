
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
    def maxSubarrays(self, nums: List[int]) -> int:
        dst = nums[0]
        ans = 0
        n = len(nums)
        for v in nums:
            dst &= v
        # print('dst' ,dst)
        if dst != 0:
            return 1
        curr = -1
        for i,v in enumerate(nums):
            if curr == -1:
                curr = v
            else:
                curr &= v
            if curr == dst:
                ans += 1
                curr = -1
            # print(i, curr, ans)
        return ans
    
# nums = [1,0,2,0,1,2]
nums = [5,7,1,3]
nums = [22,21,29,22]
sol = Solution()
print(29&22)
print(22 & 21)

print(sol.maxSubarrays(nums))
