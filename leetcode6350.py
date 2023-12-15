
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ma = 0
        ans = INF
        for i in range(len(divisors)):
            cnt = 0
            for v in nums:
                if v%divisors[i] == 0:
                    cnt += 1
            if ma < cnt:
                ma = cnt
                ans = divisors[i]
            elif ma == cnt:
                ans = min(ans, divisors[i])
        return ans
    

nums = [4,7,9,3,9]
divisors = [5,2,3]
nums = [20,14,21,10]
divisors = [5,7,5]

nums = [12]
divisors = [10,16]
sol = Solution()
print(sol.maxDivScore(nums, divisors))
