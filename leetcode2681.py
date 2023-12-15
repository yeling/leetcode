
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
    def sumOfPower(self, nums: List[int]) -> int:    
        nums.sort()
        ans = 0
        pre = 0
        for v in nums:
            ans += (pre + v) * v * v
            pre = pre * 2 + v
            pre %= MOD
            ans %= MOD
            # print(ans, pre)
        return ans
    
nums = [1,2,4,6]
sol = Solution()
print(sol.sumOfPower(nums))
