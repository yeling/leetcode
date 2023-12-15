
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
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()
        print(nums)
        for i,v in enumerate(nums):
            l = bisect_left(nums, lower - v, lo = i + 1)
            r = bisect_left(nums, upper - v + 1, lo = i + 1)
            ans += r - l
            print(l, r, ans)
        return ans
    
nums = [0,1,7,4,4,5]
lower = 3
upper = 5
nums = [1,7,9,2,5]
lower = 11
upper = 11
nums = [0,0,0,0,0,0]
lower = 0
upper = 0
sol = Solution()
print(sol.countFairPairs(nums, lower, upper))
