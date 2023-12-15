
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
    # 54 / 66
    # AC
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        preSum = 0
        ma = 0
        mi = 0
        ans = 0
        for v in nums:
            preSum += v
            ans = max(ans, abs(preSum - ma), abs(preSum - mi))
            ma = max(ma, preSum)
            mi = min(mi, preSum)
            # print(preSum)

        return ans
    

nums = [2,-5,1,-4,3,-2]
#27
# nums = [-3,-5,-3,-2,-6,3,10,-10,-8,-3,0,10,3,-5,8,7,-9,-9,5,-8]
sol = Solution()
print(sol.maxAbsoluteSum(nums))
