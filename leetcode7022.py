
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from sortedcontainers import SortedList

from typing import Optional
from heapq import *
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int: 
        sl = SortedList(nums)
        n = len(nums)
        ans = INF
        i,j = 0,0
        while i + x < n:
            while i + x > j and j < n:
                sl.remove(nums[j])
                j += 1
            u = sl.bisect_left(nums[i])
            if u != len(sl):
                ans = min(ans, abs(sl[u] - nums[i]))
            if u != 0:
                ans = min(ans, abs(sl[u - 1] - nums[i]))
            
            i += 1

        return ans

# sl = SortedList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
# sl.discard(1)
# print(sl)
# print(sl.bisect_left(13))
# print(sl.bisect_right(13))
nums = [4,3,2,4]
x = 2
nums = [71,4]
x = 1
sol = Solution()
print(sol.minAbsoluteDifference(nums, x))
