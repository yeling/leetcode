
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
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        n = len(nums)
        r = 1
        ans = 0
        while r < n:
            if nums[r] > nums[l]:
                ans += 1
                l += 1
                r += 1
            else:
                r += 1

        return ans
    
nums = [1,3,5,2,1,3,1]
nums = [1,3,2,2,4]

sol = Solution()
print(sol.maximizeGreatness(nums))
