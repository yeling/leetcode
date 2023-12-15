
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
    # 25 / 36
    def maximumSum2(self, arr: List[int]) -> int: 
        n = len(arr)
        ans = -INF  
        l = 0
        r = 0
        s = 0
        a = 0
        b = 0
        while r < n:
            if arr[r] < a:
                b = a
                a = arr[r]
            elif arr[r] < b:
                b = arr[r]
            s += arr[r]
            if s - a < 0:
                l = r + 1
                a = 0
                b = 0
                s = 0
            if r > l:
                ans = max(ans, s - a)
            ans = max(ans, arr[r])
            r += 1

        return ans
    # 25 / 36
    # AC
    def maximumSum(self, arr: List[int]) -> int: 
        #0 不删 1 删除1个
        # 子数组，删还是不删当前i个
        dp0 = arr[0]
        dp1 = 0
        ans = dp0
        for i in range(1, len(arr)):
            v = arr[i]
            dp1 = max(dp0 + v - v , dp1 + v)
            dp0 = max(dp0,0) + v
            ans = max(ans, dp0, dp1)
        return ans
    
arr = [1,-2,0,3]
# arr = [1,-2,-2,3]
# arr = [-1,-1,-1,-1]
# 7
# arr = [1,-4,-5,-2,5,0,-1,2]
sol = Solution()
print(sol.maximumSum(arr))
