
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
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]: 
        n = len(nums)
        dp = [[0] * 3 for _ in range(n)]   
        print(dp)
        return
    
nums = [1,2,1,2,6,7,5,1]
k = 2
sol = Solution()
print(sol.maxSumOfThreeSubarrays(nums, k))
