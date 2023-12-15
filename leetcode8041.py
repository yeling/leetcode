
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

def getAllFactor(num):
    ans = defaultdict(int)
    i = 2
    while i * i <= num:
        if num % i == 0:
            while num % i == 0:
                ans[i] += 1
                num //= i
        i += 1
    if num != 1:
        ans[num] += 1
    return ans

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = max(nums)
        #两个数字
        for i,v in enumerate(nums):
            f = getAllFactor(i + 1)
            m = defaultdict(int)
            for j in range(f):
                if f[j]%2 == 1:
                    m[j] = 1
                else:
                    m[j] = 0
            
            print(i + 1, f)

        return
    
nums = [8,7,3,5,7,2,4,9]
sol = Solution()
print(sol.maximumSum(nums))
