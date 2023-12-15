
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
    # 背包问题？？
    # 979 / 1502 个通过测试用例
    def numberOfWays2(self, n: int, x: int) -> int:
        ans = 0
        for i in range(19):
            if 2 ** i > n:
                ma = i
                break
        ma = n
        for i in range(1, 1 << ma):
            temp = 0
            for j in range(ma):
                if i & (1 << j) != 0:
                    temp += (j + 1) ** x
            
            if temp == n:
                # print(i, bin(i),temp)
                ans += 1
                ans %= MOD
        return ans
    
    # 979 / 1502 个通过测试用例
    def numberOfWays3(self, n: int, x: int) -> int:
        if x == 1:
            ans = 0
            dp = [1] * (n + 1)
            for i in range(1, n + 1):
                for j in range(1, (i + 1)//2):
                    dp[i] += dp[j]
                if i%2 == 0:
                    dp[i] += dp[i//2] - 1
            print(dp)
            return dp[n]
        ans = 0
        for i in range(19):
            if 2 ** i > n:
                ma = i
                break
        ma = n
        for i in range(1, 1 << ma):
            temp = 0
            for j in range(ma):
                if i & (1 << j) != 0:
                    temp += (j + 1) ** x
            
            if temp == n:
                print(i, bin(i),temp)
                ans += 1
                ans %= MOD
        return ans
    
    # 0, 1背包问题，选和不选，剩下来的数字
    # 1112 / 1502 个通过测试用例
    # AC 5380 ms
    def numberOfWays4(self, n: int, x: int) -> int:
        @cache
        def dfs(left, curr):
            # print(left, curr)
            if left < 0:
                return 0 
            if left == 0:
                return 1
            if curr > n:
                return 0
            if left - curr ** x >= 0:
                return (dfs(left, curr + 1) + dfs(left - curr ** x, curr + 1))%MOD
            else:
                return 0
        return (dfs(n, 1))%MOD
    
    # 1412 / 1502 个通过测试用例 TLE
    # AC
    def numberOfWays(self, n: int, x: int) -> int:
        #[left, index]
        dp = [[0]*(n + 1) for _ in range(n+1)]
        dp[1][n] = 1
        dp[1][n - 1] = 1
        for i in range(2,n+1):
            dp[i][:] = dp[i - 1][:]
            for j in range(n , 1, -1):
                # print(i, j)
                if j - i ** x >= 0:
                    dp[i][j - i ** x] += dp[i - 1][j]
                    dp[i][j - i ** x] %= MOD
                else:    
                    break
            # print(dp)
        return dp[n][0]% MOD


for i in count(1):
    print(i)

n = 10
x = 2
# n = 5
# x = 1
sol = Solution()
print(sol.numberOfWays4(n, x))
print(sol.numberOfWays(n, x))
