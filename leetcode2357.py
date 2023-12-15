
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
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        find = True
        
        while find:
            sub = 0
            find = False
            for i,v in enumerate(nums):
                if v > 0 and find == False:
                    find = True
                    sub = v
                    ans += 1
                    nums[i] = 0
                else:
                    nums[i] -= sub
            # print(nums)
        return ans
        
    
nums = [1,5,0,3,5]
sol = Solution()
print(sol.minimumOperations(nums))
