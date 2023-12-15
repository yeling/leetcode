
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
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        preOdd = [0] * (n + 2) 
        preEven = [0] * (n + 2)
        ans = 0
        for i,v in enumerate(nums):
            if i%2 == 0:
                preEven[i + 1] = preEven[i] + v
                preOdd[i + 1] = preOdd[i]
            else:
                preOdd[i + 1] = preOdd[i] + v
                preEven[i + 1] = preEven[i]
        # print(preEven, preOdd)
        for i in range(n):
            if preOdd[i] + preEven[n] - preEven[i + 1] == preEven[i] + preOdd[n] - preOdd[i + 1]:
                ans += 1
            
        return ans
    
nums = [2,1,6,4]
nums = [1,1,1]
sol = Solution()
print(sol.waysToMakeFair(nums))
