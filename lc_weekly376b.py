
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
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        i = 0
        n = len(nums)
        if n%3 != 0:
            return []
        ans = []
        while i < n:
            temp = [nums[i]]
            i += 1
            while len(temp) < 3 and i < n and nums[i] - temp[0] <= k:
                temp.append(nums[i])
                i += 1
            # print(temp)
            if len(temp) == 3:
                ans.append(temp)
            else:
                return []

        return ans
    
nums = [1,3,4,8,7,9,3,5,1]
k = 2
nums = [1,3,3,2,6,3]
k = 3
sol = Solution()
print(sol.divideArray(nums,k))
