
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
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = INF
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] and nums[j] > nums[k]:
                        ans = min(ans, nums[i] + nums[j] + nums[k])
        if ans == INF:
            ans = -1


        return ans
    
nums = [6,5,4,3,4,5]
sol = Solution()
print(sol.minimumSum(nums))
