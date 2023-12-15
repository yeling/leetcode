
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
    # 727 / 947 
    # 792 / 947 
    def getMaxFunctionValue2(self, receiver: List[int], k: int) -> int:
        #倍增思想, dp存储值， pos存储位置 
        #时间复杂读 n * log(k)
        n = len(receiver)
        ma = int(log(k, 2)) + 1
        dp = [[0]*ma for _ in range(n)]
        pos = [[0]*ma for _ in range(n)]
        for i in range(ma):
            for j in range(n):
                if i == 0:
                    dp[j][i] = receiver[j]
                    pos[j][i] = receiver[j]
                else:
                    middle = pos[j][i - 1]
                    dp[j][i] = dp[j][i - 1] + dp[middle][i - 1]
                    pos[j][i] = pos[middle][i - 1]
        ans = 0
        # print(dp[0])
        # print(dp[1])
        for i in range(n):
            temp = i
            next = i
            for j in range(ma):
                if k & (1 << j) != 0:
                    temp += dp[next][j]
                    next = pos[next][j]
            ans = max(ans, temp)
            # print(i, temp, ans)

        return ans
    
    # 727 / 947 
    # 792 / 947 
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        #倍增思想, dp存储值， pos存储位置 
        #时间复杂读 n * log(k)
        n = len(receiver)
        ma = int(log(k, 2)) + 1
        dp = [[0]*ma for _ in range(n)]
        pos = [[0]*ma for _ in range(n)]

        pa = [[(p,p)] + [None] * ma for p in receiver]
        print(pa)

        for i in range(ma):
            for j in range(n):
                if i == 0:
                    dp[j][i] = receiver[j]
                    pos[j][i] = receiver[j]
                else:
                    middle = pos[j][i - 1]
                    dp[j][i] = dp[j][i - 1] + dp[middle][i - 1]
                    pos[j][i] = pos[middle][i - 1]
        ans = 0
        # print(dp[0])
        # print(dp[1])
        for i in range(n):
            temp = i
            next = i
            for j in range(ma):
                if k & (1 << j) != 0:
                    temp += dp[next][j]
                    next = pos[next][j]
            ans = max(ans, temp)
            # print(i, temp, ans)

        return ans
    
receiver = [1,1,1,2,3]
k = 3
receiver = [2,0,1]
k = 4
receiver = [1,2,0]
k = 8

sol = Solution()
print(sol.getMaxFunctionValue(receiver, k))
