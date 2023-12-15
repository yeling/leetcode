
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
    def maxStrength(self, nums: List[int]) -> int:    
        self.ans = -INF
        n = len(nums)
        def dfs(index, path, res):
            if index == n:
                if len(path) > 0:
                    self.ans = max(self.ans, res)
                return
            dfs(index + 1, path, res)
            path.append(index)
            dfs(index + 1, path, res * nums[index])
            path.pop()
        dfs(0, [], 1)

        return self.ans
    
nums = [3,-1,-5,2,5,-9]
nums = [-4]
sol = Solution()
print(sol.maxStrength(nums))
