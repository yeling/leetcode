
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
    # 96 / 176 TLE 10**9
    # 1.dp，因为数据量为10**9,所以TLE 
    def minDays2(self, n: int) -> int:
        dp = [INF] * (n + 1)
        dp[n] = 0
        for i in range(n,0,-1):
            dp[i - 1] = min(dp[i-1], dp[i] + 1)
            if i%2 == 0:
                dp[i//2] = min(dp[i//2], dp[i] + 1)
            if i%3 == 0:
                dp[i//3] = min(dp[i//3], dp[i] + 1)
            # print(dp)

        return dp[0]
    
    #BFS 每次添加 (n - a)//2 , (n - b)//3
    # 175 / 176 
    def minDays(self, n: int) -> int:
        #(n,count)
        stack = defaultdict(int)
        stack[n] = 0
        ans = INF
        while len(stack) > 0:
            for k in list(stack.keys()):
                if k == 1:
                    stack[0] = stack[k] + 1
                elif k == 2 or k == 3:
                    stack[0] = stack[k] + 2
                else:
                    if k//2 not in stack:  
                        stack[k//2] = stack[k] + 1 + k%2
                    else:
                        stack[k//2] = min(stack[k//2], stack[k] + 1 + k%2)
                    
                    if k//3 not in stack:
                        stack[k//3] = stack[k] + 1 + k%3
                    else:
                        stack[k//3] = min(stack[k//3], stack[k] + 1 + k%3)
                if 0 in stack:
                    ans = min(ans, stack[0])
                del stack[k]
            # print(stack)
            if len(stack) == 1 and 0 in stack:
                break
        return ans
    
n = 17
n = 1
sol = Solution()
print(sol.minDays2(n))
print(sol.minDays(n))
