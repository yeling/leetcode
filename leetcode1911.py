
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
    def maxAlternatingSum(self, nums: List[int]) -> int:
        oddSum = 0
        evenSum = 0    
        for v in nums:
            nextOdd = max(oddSum, evenSum + v)
            nextEven = max(evenSum, oddSum - v)
            oddSum = nextOdd
            evenSum = nextEven
        
        return max(oddSum, evenSum)
    
nums = [4,2,5,3]
nums = [5,6,7,8]
sol = Solution()
print(sol.maxAlternatingSum(nums))
