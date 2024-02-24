
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
    #单调栈
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        ans = INF
        n = len(nums)
        i = 1
        #(pos,value)
        # stack = deque()
        temp = []
        while i < k and i < n:
            temp.append((nums[i], i))
            i += 1
        temp.sort(reverse=True)
        stack = deque(temp)
        while i <= 1 + dist and i < n:
            

        # curr = 0
        # while i < n:
        #     while len(stack) > 0 and i - stack[0][0] > dist:
        #         curr -= stack[0][1]
        #         stack.popleft()
        #     if len(stack)


        return
    
nums = [1,3,2,6,4,2]
k = 3
dist = 3
sol = Solution()
print(sol.minimumCost(nums, k, dist))
