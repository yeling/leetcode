
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:    
        for v in nums:
            v.sort()
        m = len(nums)
        n = len(nums[0])
        ans = 0
        # print(nums)
        for i in range(n):
            temp = 0
            for j in range(m):
                temp = max(temp, nums[j][i])
            ans += temp

        return ans
    
nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
sol = Solution()
print(sol.matrixSum(nums))
