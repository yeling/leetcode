
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        conver = [0] * n
        ma = nums[0]
        for i,v in enumerate(nums):
            ma = max(ma,v)
            conver[i] = v + ma
        # print(conver)
        ans = [0] * (n + 1)
        for i,v in enumerate(conver):
            ans[i + 1] = ans[i] + v

        return ans[1:]
    
nums = [1,1,2,4,8,16]
nums = [2,3,7,5,10]
sol = Solution()
print(sol.findPrefixScore(nums))
