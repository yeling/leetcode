
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def maximumOr2(self, nums: List[int], k: int) -> int:
        ma = 0
        index = -1
        for i,v in enumerate(nums):
            if v > ma:
                ma = v
                index = i
        ans = 0
        for i,v in enumerate(nums):
            if i != index:
                ans |= v
        ans |= (ma << k)
        return ans
    
    def maximumOr(self, nums: List[int], k: int) -> int:
        cnt = [0]*32
        def toInt(cnt):
            num = 0
            for i in range(len(cnt)):
                if cnt[i] >= 1:
                    num += (1<<i)
            return num
        sumor = 0
        for i,v in enumerate(nums):
            sumor |= v
            temp = bin(v)[2:]
            for i in range(len(temp)):
                if temp[-1-i] == '1':
                    cnt[i] += 1
        # print(toInt(cnt))
        ans = 0
        for v in nums:
            tempCnt = cnt[:]
            temp = bin(v)[2:]
            for i in range(len(temp)):
                if temp[-1-i] == '1':
                    tempCnt[i] -= 1
            ans = max(ans, toInt(tempCnt) | (v << k))

        # print(cnt)
            
       
        return ans
    
nums = [12,9]
k = 1
# nums = [18,8,20]
# k = 1

sol = Solution()
print(sol.maximumOr2(nums,k))
print(sol.maximumOr(nums,k))
