
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
    # 434 / 533 个
    def minSizeSubarray(self, nums: List[int], target: int) -> int: 
        n = len(nums)
        s = sum(nums)
        base = 0
        if target >= s:
            base += (target//s) * n
        target %= s
        if target == 0:
            return base

        nums = nums[:] + nums[:]
        pre = [0] * (2*n + 1)
        cache = defaultdict(int)
        ans = INF
        for i,v in enumerate(nums):
            pre[i + 1] = pre[i] + v
            if pre[i + 1] - target in cache:
                ans = min(ans, i - cache[pre[i + 1] - target])
            cache[pre[i + 1]] = i
        if ans == INF:
            return -1
        return ans + base
    
nums = [1,2,3]
target = 5
nums = [1,1,1,2,3]
target = 4
nums = [2,4,6,8]
target = 3
nums = [1,2,2,2,1,2,1,2,1,2,1]
target = 83

nums = [17,4,3,14,17,6,15]
target = 85

nums = [1,6,5,5,1,1,2,5,3,1,5,3,2,4,6,6]
target = 56

sol = Solution()
print(sol.minSizeSubarray(nums, target))
