
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
    def summaryRanges(self, nums: List[int]) -> List[str]:  
        n = len(nums)
        ans = []
        if n == 0:
            return ans
        curr = nums[0]
        start = curr
        
        for i in range(1,n):
            if curr + 1 == nums[i]:
                curr = nums[i]
            else:
                if curr == start:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + "->" + str(curr))
                curr = start = nums[i]

        if curr == start:
            ans.append(str(start))
        else:
            ans.append(str(start) + "->" + str(curr))
        

        return ans
    
nums = [0,1,2,4,5,7]
nums = [0,2,3,4,6,8,9]
sol = Solution()
print(sol.summaryRanges(nums))
