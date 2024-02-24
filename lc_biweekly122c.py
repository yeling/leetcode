
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
    def minimumArrayLength(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        s = nums[0]
        ans = 0
        for i in range(n):
            if nums[i] == s:
                ans += 1
            elif nums[i]%s != 0:
                return 1

        return (ans + 1)//2
    
nums = [1,4,3,1]
nums = [5,5,5,10,5]
nums = [2,3,4]
sol = Solution()
print(sol.minimumArrayLength(nums))
