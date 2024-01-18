
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
    # 723 / 948
    # 906 / 948 个通过测试用例
    # 945 / 948 个通过测试用例

    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if y >= x:
            return y - x
        
        dp = [INF] *  (x + 30)
        dp[x] = 0
        s = x + 11
        e = min(-1, y - 12)
        for i in range(s, e, -1):
            for j in range(i, i + 12):
                dp[j] = min(dp[j], dp[j - 1] + 1)
                if j % 11 == 0:
                    dp[j//11] = min(dp[j//11], dp[j] + 1)
                if j%5 == 0:
                    dp[j//5] = min(dp[j//5], dp[j] + 1)
                                    
            if i % 11 == 0:
                dp[i//11] = min(dp[i//11], dp[i] + 1)
            if i%5 == 0:
                dp[i//5] = min(dp[i//5], dp[i] + 1)
            dp[i - 1] = min(dp[i - 1], dp[i] + 1)

            # print(i, dp)
        for i in range(y):
            dp[y] = min(dp[y], dp[i] + y - i)

        return dp[y]
    
x = 26
y = 1
# x = 54
# y = 2

# x = 25
# y = 30
x = 5
y = 3
#34 47
x = 97
y = 50
x = 55
y = 20


sol = Solution()
print(sol.minimumOperationsToMakeEqual(x, y))
