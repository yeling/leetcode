
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

# 1250. 检查「好数组」
MOD = 10 ** 9 + 7

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        g = nums[0]
        for v in nums:
            g = gcd(g,v)
        return g == 1
         

nums = [12,5,7,23]
nums = [3,6]
nums = [1]
sol = Solution()
print(sol.isGoodArray(nums))
