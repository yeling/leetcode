
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
    def sumOfPower2(self, nums: List[int]) -> int:
        self.ans = 0
        def dfs(index, path):
            # print(index, path)
            if index == len(nums):
                if len(path) > 0:
                    self.ans = (self.ans + max(path) * max(path) * min(path))%MOD
                return
                
            dfs(index + 1,path)
            path.append(nums[index])
            dfs(index + 1, path)
            path.pop()

        path = []
        dfs(0,path)
        return self.ans
    
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        # print(nums)
        last = 0
        for i,v in enumerate(nums):
            curr = 0
            if i > 0:
                last = 2 * last + nums[i - 1]
            curr = v + last
            temp = (v * v * curr)%MOD
            ans = (ans + temp)%MOD
            # print(ans, temp)
        return ans
    
nums = [2,1,4]
# 13928461
nums = [76,24,96,82,97]
# nums = [1,2,3,4]
sol = Solution()
print(sol.sumOfPower2(nums))
print(sol.sumOfPower(nums))
