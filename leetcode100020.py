
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
    def minLengthAfterRemovals(self, nums: List[int]) -> int:  
        c = Counter(nums)
        n = len(nums)
        ma = c.most_common(1)
        # print(ma)  
        if ma[0][1] <= n//2:
            return n%2
        else:
            return n - (n - ma[0][1]) * 2
        return
    
nums = [1,1,2]
nums = [1,3,4,9]
nums = [2,3,6]
sol = Solution()
print(sol.minLengthAfterRemovals(nums))
