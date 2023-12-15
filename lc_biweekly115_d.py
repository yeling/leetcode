
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
    # 609 / 643 个通过测试用例
    # 611 / 643 个通过测试用例
    # 627 / 643 TLE 
    def countSubMultisets2(self, nums: List[int], l: int, r: int) -> int:
        ma = 2 * 10000 + 1
        # ma = 17
        n = len(nums)
        ans = 0
        dp = [0] * (ma)
        cache = defaultdict(int)
        for v in nums:
            cache[v] += 1
        for i in cache.keys():
            # print(i)
            next = [0] * (ma)
            for j in range(ma):
                if dp[j] != 0:
                    for c in range(cache[i] + 1):
                        if j + i * c > r:
                            break
                        next[j + i * c] += dp[j]

            for c in range(1, cache[i] + 1):
                if i * c > r:
                    break
                next[i * c] += 1
            dp = next
            # print(dp)
        for i in range(l, r + 1):
            ans += dp[i]
            ans %= MOD
        if l == 0:
            ans += 1
        return ans % MOD
    
    def countSubMultisets3(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = 0
        dp = [0] * (r + 1)
        dp[0] = 1
        cache = defaultdict(int)
        for v in nums:
            cache[v] += 1
        for i in cache.keys():
            # print(i)
            next = [0] * (r + 1)
            for j in range(r, -1, -1):
                for c in range(0, cache[i] + 1):
                    if j - i * c >= 0:
                        # print(i, j+1, j + 1 - i * c)
                        next[j] += dp[j - i * c]
            dp = next
            # print(dp)
        for i in range(l, r + 1):
            ans += dp[i]
            ans %= MOD
        
        return ans % MOD
    
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = 0
        dp = [0] * (r + 1)
        dp[0] = 1
        cache = defaultdict(int)
        for v in nums:
            cache[v] += 1
        for i in cache.keys():
            # print(i)
            next = [0] * (r + 1)
            for j in range(r, -1, -1):
                for c in range(0, cache[i] + 1):
                    if j - i * c >= 0:
                        # print(i, j+1, j + 1 - i * c)
                        next[j] += dp[j - i * c]
            dp = next
            # print(dp)
        for i in range(l, r + 1):
            ans += dp[i]
            ans %= MOD
        
        return ans % MOD
    
nums = [2,1,4,2,7]
l = 1
r = 5
nums = [1,2,1,3,5,2]
l = 3
r = 5
# nums = [0,0,0,0,0]
# l = 0
# r = 0
sol = Solution()
print(sol.countSubMultisets2(nums, l, r))
print(sol.countSubMultisets(nums, l, r))
