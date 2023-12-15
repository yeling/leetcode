
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
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        ans = 0
        zero = 0
        one = 0
        # 原来的0 + (原来的0 + 新的0) + 新的0
        for v in nums:
            if v == 0:
                zero = (zero + zero + 1)%MOD
            elif v == 1:
                one = (one + one + zero)%MOD
            elif v == 2:
                ans = (ans + ans + one)%MOD       
            # print(i, zero, one, two)
        return ans%MOD
    
nums = [0,1,2,2]
nums = [0,1,2,0,1,2]
sol = Solution()
print(sol.countSpecialSubsequences(nums))
