
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
    def differenceOfSum(self, nums: List[int]) -> int:
        s1 = sum(nums)
        s2 = 0
        for v in nums:
            while v > 0:
                s2 += v%10
                v //= 10
        
        return abs(s1 - s2)
    
nums = [1,2,3,4]
# nums = [1,15,6,3]
sol = Solution()
print(sol.differenceOfSum(nums))
