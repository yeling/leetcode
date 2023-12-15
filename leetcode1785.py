
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
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s = sum(nums)
        # print(s)
        if goal >= s:
            return (goal - s + limit - 1)//limit
        else:
            return (s - goal + limit - 1)//limit
    
nums = [1,-1,1]
limit = 3
goal = -4
sol = Solution()

nums = [1,-10,9,1]
limit = 100
goal = 0

#25322847
nums = [2,2,2,5,1,-2]
limit = 5
goal = 126614243

print(sol.minElements(nums, limit, goal))
# print(goal//5)