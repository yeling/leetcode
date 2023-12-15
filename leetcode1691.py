
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
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # print(cuboids)
        for v in cuboids:
            v.sort()
        cuboids.sort(key=sum)
        # print(cuboids)
        n = len(cuboids)
        dp = [0] * n
        ans = 0
        for i in range(n):
            dp[i] = cuboids[i][2]
            for j in range(i):
                if cuboids[i][0] >= cuboids[j][0] and cuboids[i][1] >= cuboids[j][1] and cuboids[i][2] >= cuboids[j][2]:
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])
            ans = max(ans, dp[i])

        return ans
    

cuboids = [[50,45,20],[95,37,53],[45,23,12]]
sol = Solution()
print(sol.maxHeight(cuboids))
