
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
    # 520 / 2556 个通过测试用例
    # 1079 / 2556 个通过测试用例
    def paintWalls2(self, cost: List[int], time: List[int]) -> int:    
        n = len(cost)
        dp = [0] * n
        # maxt = 501
        maxt = 4
        for i in range(n):
            dp[i] = [[10]*maxt for i in range(2)]
        ans = INF
        # 1 付费, 0 免费
        dp[0][1][time[0]] = cost[0]
        for i in range(1,n):
            for j in range(0,i):
                for t in range(1,maxt):
                    # 0 - 0
                    dp[i][0][t - 1] = min(dp[i][0][t - 1], dp[j][0][t], dp[j][1][t])
                    # 1 - 1
                    dp[i][1][time[i]] = min(dp[i][1][time[i]],dp[j][1][t - 1] +  cost[i], dp[j][0][t - 1] +  cost[i])            
        
            print(dp)
            
        for t in range(1,maxt):
            ans = min(ans, dp[n-1][1][t - 1], dp[n-1][0][t - 1])
        return ans
    
    #523  dp错误，墙不需要顺序
    def paintWalls3(self, cost: List[int], time: List[int]) -> int:   
        n = len(cost)
        def f(cost: List[int], time: List[int]) :
            dp = [0] * n
            maxt = 501
            # maxt = 4
            for i in range(n):
                dp[i] = [[INF]*maxt for i in range(2)]
            ans = INF
            # 1 付费, 0 免费
            dp[0][1][time[0]] = cost[0]
            for i in range(1,n):
                j = i -1
                for t in range(1,maxt):
                    # 0 - 0
                    dp[i][0][t - 1] = min(dp[i][0][t - 1], dp[j][0][t], dp[j][1][t - 1])
                    # 1 - 1
                    dp[i][1][time[i]] = min(dp[i][1][time[i]],dp[j][1][t - 1] +  cost[i], dp[j][0][t - 1] +  cost[i])
                # print(dp)            
            for t in range(1,maxt):
                ans = min(ans, dp[n-1][1][t - 1], dp[n-1][0][t - 1])
            return ans
        ans = INF
        for i in range(n):
            temp = cost[i:] + cost[0:i]
            tempTime = time[i:] + time[0:i]
            ans = min(ans, f(temp, tempTime))
            print(i, ans, temp, tempTime)
        return ans
    
    def paintWalls(self, cost: List[int], time: List[int]) -> int:   
        n = len(cost)
        #dfs，从后往前考虑，前面i个，剩余时间为j
        @cache
        def dfs(i, j):
            if j >= i + 1:
                return 0
            if i < 0:
                return INF            
            return min( cost[i] + dfs(i-1, j + time[i]), dfs(i-1, j - 1))
        return dfs(n-1,0)
    
cost = [1,2,3,3]
time = [1,2,3,2]
# cost = [2,3,4,2]
# time = [1,1,1,1]
# cost = [8,7,5,15]
# time = [1,1,2,1]
# 63
# cost = [42,8,28,35,21,13,21,35]
# time = [2,1,1,1,2,1,1,2]
sol = Solution()
print(sol.paintWalls(cost, time))
