
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
    def xorBeauty(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]  
        return ans
    
nums = [1,4]
nums = [15,45,20,2,34,35,5,44,32,30]
sol = Solution()
print(sol.xorBeauty(nums))
