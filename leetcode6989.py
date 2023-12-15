
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
    def maxSum(self, nums: List[int], m: int, k: int) -> int:  
        n = len(nums)
        ans = 0
        cache = defaultdict(int)
        tempSum = 0
        for i in range(n):
            if i - k >= 0:
                tempSum -= nums[i - k]
                cache[nums[i - k]] -= 1
                if cache[nums[i - k]] == 0:
                    del cache[nums[i - k]] 
            cache[nums[i]] += 1
            tempSum += nums[i]
            
            if len(cache) >= m:
                ans = max(ans, tempSum)
                     
        return ans
    
nums = [2,6,7,3,1,7]
m = 3
k = 4
nums = [5]
m = 1
k = 1
sol = Solution()
print(sol.maxSum(nums, m, k))
