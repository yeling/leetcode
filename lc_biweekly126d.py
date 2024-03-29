
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

def quickPowMode(a, n, p):
    ans = 1
    while(n > 0):
        if n & 1 == 1:
            ans = ans * a % p
        a = a * a % p
        n = n >> 1
    return ans % p

class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for v in nums:
            next = []
            for d in dp:
                next.append(d[:])
            for i in range(n):
                for j in range(k):
                    if j + v <= k and dp[i][j] > 0:
                        next[i + 1][j + v] += dp[i][j]
            if v <= k:
                next[1][v] += 1
            dp = next
            # print(dp)

        ans = 0
        
        for i in range(1,n+1):
            ans += (dp[i][k] * quickPowMode(2, n - i,MOD))%MOD
            

        return ans%MOD
    
nums = [1,2,3]
k = 3
nums = [2,3,3]
k = 5
nums = [1,2,3]
k = 7
nums = [3]
k = 1
sol = Solution()
print(sol.sumOfPower(nums, k))
