
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
    def sumOfEncryptedInt(self, nums: List[int]) -> int:   
        sum = 0
        for v in nums:
            t = v
            va = []
            while t > 0:
                va.append(t%10)
                t //= 10
            
            ma = max(va)
            # print(ma)
            re = ""
            for i in range(len(str(v))):
                re += str(ma)
            
            # print(re)
            sum += int(re) 
        return sum
    
nums = [10,21,31]
sol = Solution()
print(sol.sumOfEncryptedInt(nums))
