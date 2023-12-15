
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
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:    
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i]%2 == 1 or nums[i] > threshold:
                continue
            l = i
            r = i
            while r < n - 1 and nums[r] <= threshold and nums[r + 1] <= threshold and nums[r]%2 != nums[r + 1]%2:
                r += 1
            ans = max(ans, r - l + 1)
        return ans
    
nums = [3,2,5,4]
threshold = 5
# nums = [2,3,4,5]
# threshold = 4
nums = [1,2]
threshold = 2

nums = [4]
threshold = 1

sol = Solution()
print(sol.longestAlternatingSubarray(nums, threshold))
