
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

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        cache = [[] for _ in range(10)]
        for v in nums:
            temp = [int(vi) for vi in str(v)]
            cache[max(temp)].append(v)
        # print(cache)
        ans = -1
        for i in range(1,10):
            cache[i].sort(reverse=True)
            if len(cache[i]) >= 2:
                ans = max(ans, cache[i][0] + cache[i][1])

        return ans
    
nums = [51,71,17,24,42]
nums = [1,2,3,4]
nums = [84,91,18,59,27,9,81,33,17,58]
sol = Solution()
print(sol.maxSum(nums))
