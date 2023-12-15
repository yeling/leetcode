
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
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:

    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        vis = [False] * 101
        for i in range(1,101):
            for s,e in nums:
                if i >= s and i <= e:
                    vis[i] = True
        ans = 0
        for v in vis:
            if v:
                ans += 1
        
        return ans
    
nums = [[3,6],[1,5],[4,7]]
nums = [[1,3],[5,8]]
# nums = [[2,5],[3,8],[1,6],[4,10]]
nums = [[9,9],[2,8],[5,8],[3,5],[2,2],[7,9],[5,10]]
sol = Solution()
print(sol.numberOfPoints(nums))
