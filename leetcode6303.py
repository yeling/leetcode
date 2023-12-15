
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
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for v in nums:
            temp = []
            # temp.append(v%10)
            while v > 0:
                temp.append(v%10)
                v //=10
            # print(temp)
            for i in range(len(temp)):
                ans.append(temp[-1-i])
                 
        return ans
    
nums = [13,25,83,77]
nums = [7,1,3,9]
sol = Solution()
print(sol.separateDigits(nums))
