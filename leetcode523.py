
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
    # 81 / 99
    # 87 / 99 
    # 89 / 99 
    def checkSubarraySum2(self, nums: List[int], k: int) -> bool:
        cache = defaultdict(int)
        n = len(nums)
        pre = 0
        for i in range(n):
            pre += nums[i]
            if cache[pre%k] == 1 or (pre != 0 and pre%k == 0):
                return True
            if pre >= k:
                pre %= k
                cache[pre] = 1
        # print(cache)
        return False
    # 81 / 99
    # 87 / 99 
    # 89 / 99 
    # 92 / 99
    # 95 / 99 
    def checkSubarraySum3(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        pre = [0] * (n + 1)
        for i,v in enumerate(nums):
            pre[i + 1] = pre[i] + v
        
        cache = defaultdict(int)
        for i in range(n):
            if cache[pre[i + 1]%k] == 1 or (pre[i + 1]%k == 0 and i > 0):
                return True
            cache[pre[i + 1]%k] = 1
            # print(cache)
        return False
    
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        pre = [0] * (n + 1)
        last = -1
        #连续连个0，为True
        for i,v in enumerate(nums):
            pre[i + 1] = pre[i] + v
            if last == 0 and v == 0:
                return True
            last = v
        
        cache = defaultdict(int)
        for i in range(n):
            last = cache[pre[i + 1]%k]
            if (pre[i + 1] >= k and cache[pre[i + 1]%k] != 0) and i + 1 - cache[pre[i + 1]%k] >= 2:
                return True
            if (pre[i + 1]%k == 0 and i > 0):
                return True
            if cache[pre[i + 1]% k] == 0:
                cache[pre[i + 1]% k] = i + 1

            # print(cache)
        return False
    
# nums = [23,2,4,6,6]
# k = 7

nums = [1,2,12]
k = 12

sol = Solution()
print(sol.checkSubarraySum(nums, k))
