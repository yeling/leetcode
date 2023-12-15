
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
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans = 0
        pre = 0
        for i,v in enumerate(nums):
            pre += v
            if pre > 0:
                ans += 1
            else: 
                break
        return ans
    
nums = [2,-1,0,1,-3,3,-3]
# nums = [-2,-3,0]
# nums = [-687767,-860350,950296,52109,510127,545329,-291223,-966728,852403,828596,456730,-483632,-529386,356766,147293,572374,243605,931468,641668,494446]
sol = Solution()
print(sol.maxScore(nums))
