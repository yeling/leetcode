
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
    def minGroupsForValidAssignment2(self, nums: List[int]) -> int:
        n = len(nums)
        cache = defaultdict(int)
        for v in nums:
            cache[v] += 1
        vs = list(cache.values())
        print(vs)
        def check(x, y):
            a = x//y
            b = x%y
            if a >= b:
                return True
            else:
                return False
            return 
        l = 1
        r = max(vs)
        while l <= r:
            mid = l + (r - l)//2
            t = True
            for v in vs:
                t &= check(v, mid)
                if t == False:
                    break
            if t == False:
                r = mid - 1
            elif t == True:
                l = mid + 1
        cnt = l - 1
        print(cnt)
        ans = 0
        for v in vs:
            ans += v//(cnt + 1) 
            if v%(cnt + 1):
                ans += 1    
        return ans
    
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        n = len(nums)
        cache = defaultdict(int)
        for v in nums:
            cache[v] += 1
        vs = list(cache.values())
        # print(vs)
        def check(x, y):
            a = x//y
            b = x%y
            if a >= b:
                return True
            else:
                return False
            return 
        l = 1
        r = max(vs)
        cnt = 1
        for i in range(1, r + 1):
            t = True
            for v in vs:
                t &= check(v, i)
                if t == False:
                    break
            if t:
                cnt = i
        ans = 0
        for v in vs:
            ans += v//(cnt + 1) 
            if v%(cnt + 1):
                ans += 1    
        return ans
    
    
nums = [3,2,3,2,3]
# nums = [10,10,10,3,1,1]
# nums = [1,1,1,1,1]
sol = Solution()
print(sol.minGroupsForValidAssignment(nums))
