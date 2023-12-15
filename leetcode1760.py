
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def minimumSize2(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)
        t = maxOperations
        #1.最终结果需要等于，如果在r中判断等于
        #mid - 1是可能等于l的，所以while l <= r
        # l = r + 1
        while l <= r:
            mid = l + (r - l)//2
            curr = 0
            for v in nums:
                curr += (v + mid - 1)//mid - 1
            if t < curr:
                l = mid + 1  
            elif t >= curr:
                r = mid - 1
        return l
    
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)
        t = maxOperations
        #1.最终结果需要等于，如果在l中判断等于，说明l不能再走了
        #mid + 1是可能等于r的，所以while l < r
        #2. l == r
        while l < r:
            mid = l + (r - l)//2
            curr = 0
            # print(l,r,mid)
            for v in nums:
                curr += (v + mid - 1)//mid - 1
            if t <= curr:
                l = mid + 1  
            elif t > curr:
                r = mid - 1
            
        return l - 1
    
nums = [9]
maxOperations = 2

# maxOperations = 4
# nums = [2,4,8,2]

sol = Solution()
print(sol.minimumSize(nums,maxOperations))
