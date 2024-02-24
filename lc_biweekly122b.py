
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
    def canSortArray(self, nums: List[int]) -> bool:
        ns = nums[:]
        ns.sort()
        n = len(nums)
    
        for i in range(n):
            p = bisect_left(ns, nums[i])
            tar = bin(nums[i]).count("1")
            s = min(i, p)
            e = max(i, p)
            for j in range(s,e+1):
                if bin(nums[j]).count("1") == tar:
                    continue
                else:
                    return False
            # print(tar)

        return True
    
nums = [8,4,2,30,15]
nums = [3,16,8,4,2]
sol = Solution()
print(sol.canSortArray(nums))
