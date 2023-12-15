
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
    # 52 / 84
    # 53 / 84 TLE
    def mergeStones2(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if n == 1:
            return 0
        if (n - 1)%(k - 1) != 0 or n < k:
            return -1
        @cache
        def dfs(curr):
            if len(curr) == k:
                return sum(curr)
            ans = INF
            for i in range(len(curr) - k + 1):
                subArray = curr[0:i] +tuple([sum(curr[i:i + k])]) + curr[i+k:]
                # print(subArray)
                ans = min(ans, sum(curr[i:i + k]) + dfs(subArray))
            
            return ans

        return dfs(tuple(stones))
    
    # 62 / 84
    def mergeStones3(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if n == 1:
            return 0
        if (n - 1)%(k - 1) != 0 or n < k:
            return -1
        
        @cache
        def dfs(curr):
            if len(curr) == k:     
                return sum(curr)
            ans = INF
            for i in range(len(curr) - k + 1):
                subArray = curr[0:i] +tuple([sum(curr[i:i + k])]) + curr[i+k:]
                # print(subArray)
                ans = min(ans, sum(curr[i:i + k]) + dfs(subArray))
                # print(subArray)
            return ans

        return dfs(tuple(stones))
    
    def mergeStones(self, stones: List[int], k: int) -> int:
        INF = 1000
        n = len(stones)
        if n == 1:
            return 0
        if (n - 1)%(k - 1) != 0  or n < k:
            return -1
        ans = INF
        #dp[i][j][k] i 到 j 合并为k份的最小值 1...k-1
        dp = [[[INF] * (k + 1) for _ in range(n)] for _ in range(n)]
        # print(dp[0][0][0])
        for ik in range(1,k+1):
            for i in range(n):
                for j in range(i, n):
                    if ik == 1:
                        dp[i][j][ik] = min(dp[i][j][ik],sum(stones[i:j+1]))
                    else:
                        for m in range(i,j):
                            for mk in range(1,ik):
                                dp[i][j][ik] = min(dp[i][j][ik], dp[i][m][mk] + dp[m+1][j][ik - mk])

        print(dp)
        ans = dp[0][n-1][k]

        return ans + sum(stones)
    

stones = [3,5,1,2,6]
k = 3

# stones = [1]
# k = 2

# stones = [6,4,4,6]
# k = 2


sol = Solution()
print(sol.mergeStones2(stones, k))

print(sol.mergeStones(stones, k))

