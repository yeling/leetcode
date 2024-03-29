
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
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        cache = []
        n = len(nums)
        flag = [False] * n
        for i,v in enumerate(nums):
            heappush(cache,(v,i))
        s = sum(nums)
        ans = []
        for i,k in queries:
            if flag[i] == False:
                flag[i] = True
                s -= nums[i]
            for _ in range(k):
                while len(cache) > 0:
                    t = heappop(cache)
                    if flag[t[1]] == False:
                        s -= t[0]
                        flag[t[1]] = True
                        break
            ans.append(s)
            # print(s, flag)



        return ans
    
nums = [1,2,2,1,2,3,1]
queries = [[1,2],[3,3],[4,2]]
nums = [1,4,2,3]
queries = [[0,1]]
sol = Solution()
print(sol.unmarkedSumArray(nums, queries))

