
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    # ans + n - (i + 1) i+1已经排序好了，重复了
    # i 在 i - 1 的左侧，加一轮
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:   
        cache = []
        n = len(nums)
        for i,v in enumerate(nums):
            cache.append([v,i])
        cache.sort()
        # for i,v in enumerate(cache):
        #     v[0] = i
        print(cache)
        ans = n
        for i,v in enumerate(cache):
            if i > 0 and cache[i - 1][1] > v[1]:
                ans = ans + n - i

        return ans
    
nums = [1,2,4,3]
# nums = [4,1,2]
nums = [-4,-13,-12]
sol = Solution()
print(sol.countOperationsToEmptyArray(nums))
