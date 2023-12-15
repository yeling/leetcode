
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
    # 91 / 98
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        n = len(nums)
        m = len(groups)
        ans = False
        pi = 0
        j = 0
        while pi < n and j < m:
            #1.find first
            while pi < n:
                if nums[pi] == groups[j][0]:
                    break
                pi += 1
            #2.find group[j]
            k = 0
            ki = pi
            while ki < n and k < len(groups[j]):
                if nums[ki] == groups[j][k]:
                    ki += 1
                    k += 1
                else:
                    break
            #3.check
            if k == len(groups[j]):
                j += 1
                pi = ki
            else:
                pi += 1
        if j == m:
            ans = True
        return ans

groups = [[1,-1,-1],[3,-2,0]]
nums = [0,1,-1,-1,5,3,-2,3,-2,0]

# groups = [[-5,0]]
# nums = [2,0,-2,5,-1,2,4,3,4,-5,-5]

sol = Solution()
print(sol.canChoose(groups, nums))
