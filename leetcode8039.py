
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
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        first = -1
        for i in range(1,n):
            if nums[i] > nums[i - 1]:
                continue
            else:
                if first == -1:
                    first = i
                else:
                    return -1
        if first == -1:
            return 0
        elif first != -1 and nums[-1] < nums[0]:
            return n - first
        else:
            return -1


    
nums = [3,4,5,1,2]
nums = [1,3,5]
nums = [2,1,4,3,0]
sol = Solution()
print(sol.minimumRightShifts(nums))
