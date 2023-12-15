
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        #1.将arr转化为在target中的位置
        #2.在arr中照LIS，最长上升子序列
        tc = {v:i for i,v in enumerate(target)}
        for i,v in enumerate(arr):
            if v in tc:
                arr[i] = tc[v]
            else:
                arr[i] = -1

        #2.LIS
        cache = []
        # cache.append(arr[0])
        for v in arr:
            if v == -1:
                continue
            index = bisect_left(cache, v)
            if index == len(cache):
                cache.append(v)
            elif v < cache[index]:
                cache[index] = v
            
        # print(tc, arr)
        # print(len(cache))
        return len(target) - len(cache)

target = [6,4,8,1,3,2]
arr = [4,7,6,2,3,8,6,1]
target = [5,1,3]
arr = [9,4,2,3,4]

# sol = Solution()
# print(sol.minOperations(target, arr))
