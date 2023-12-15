
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
    # 41 / 69 
    def minDistance2(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses.sort()
        #1.计算相邻点的距离dis,index
        #2.移除最大的几个点
        #3.计算最短距离，双指针偶数点取中间，奇数点最后一个点为0
        stack = PriorityQueue()
        vis = [False] * n
        vis[n - 1] = True
        for i in range(n-1):
            stack.put([-(houses[i + 1] - houses[i]), i])
        for i in range(k-1):
            curr = stack.get()
            vis[curr[1]] = True
        print(vis)
        s = 0
        e = 0
        ans = 0
        while e < n:
            if vis[e] == True:
                #计算l到e的距离
                l,r = s,e
                print(s, e)
                while l < r:
                    ans += houses[r] - houses[l]
                    l += 1
                    r -= 1
                s = e + 1
            e += 1
            
        return ans

    def minDistance(self, houses: List[int], k: int) -> int:
        #1. n == 100, n^3的动态规划
        #2.dp[i][j] 前i个房子，j个邮筒最短距离
        #3.dp[i][j] = min(dp[k][j - 1] + cost[k,i])
        n = len(houses)
        dp = [[INF] * (n + 1) for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        houses.sort()
        for i in range(n):
            for j in range(i + 1, n):
                l = i
                r = j
                temp = 0
                while l < r:
                    temp += houses[r] - houses[l]
                    r -= 1
                    l += 1
                cost[i][j] = temp
        # print(cost)
        for i in range(n):
            dp[i][i+1] = 0
            dp[i][1] = cost[0][i]
            for j in range(2, min(i + 1,k + 1)):
                for d in range(0,i):
                    dp[i][j] = min(dp[i][j], dp[d][j - 1] + cost[d + 1][i])
            # print(dp)
        return dp[n-1][k]

    
houses = [1,4,8,10,20]
k = 3
# houses = [2,3,5,12,18]
# k = 2
houses = [14,2,5,7,10]
k = 2

sol = Solution()
print(sol.minDistance(houses,k))
