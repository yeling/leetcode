
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
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:    
        n = len(nums)
        cache = [(v,i) for i,v in enumerate(nums)]
        cache.sort()
        ans = [-1] * (n)
        for i,v in enumerate(nums):
            if ans[i] != -1:
                continue
            curr = [i]
            pp = bisect_left(cache,(v,i))
            suf = pp + 1
            while suf < n and cache[suf][0] - cache[suf - 1][0] <= limit:
                curr.append(cache[suf][1])
                suf += 1
            pre = pp - 1
            while pre >= 0 and cache[pre + 1][0] - cache[pre][0] <= limit:
                curr.append(cache[pre][1])
                pre -= 1
            # print(curr)
            org = []
            for v in curr:
                org.append(nums[v])
            org.sort()
            curr.sort()
            for j in range(len(curr)):
                ans[curr[j]] = org[j]
            # print(ans, org)

        return ans
    
nums = [1,5,3,9,8]
limit = 2
# nums = [1,7,6,18,2,1]
# limit = 3
nums = [1,7,28,19,10]
limit = 3
sol = Solution()
print(sol.lexicographicallySmallestArray(nums, limit))
