
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
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            for j in range(i,n):
                if abs(nums[i] - nums[j]) >= valueDifference and abs(i - j) >= indexDifference:
                    ans = [i,j]
                    return ans

        return [-1, -1]
    
nums = [5,1,4,1]
indexDifference = 2
valueDifference = 4
sol = Solution()
print(sol.findIndices(nums, indexDifference, valueDifference))
