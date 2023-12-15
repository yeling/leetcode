
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
    #
    def countPalindromes(self, s: str) -> int:
        #1.计算每个位置 00-99出现的次数
        #2.计算0 到 i-1 01, 和i+1到 n - 1中  10 类似的出现次数，乘起来
        #3.从后面往前计算 10出现的次数
        #
        n = len(s)
        def getDp(s:str):
            n = len(s)
            #存储 00-99
            dp = [defaultdict(int) for _ in range(n)]
            #存储 0 - 9
            dpTen = defaultdict(int)
            for i in range(0,n):
                if i > 0:
                    for j in range(10):
                        for k in range(10):
                            dp[i][str(j) + str(k)] = dp[i - 1][str(j) + str(k)]
                    for j in range(10):
                        dp[i][str(j) + s[i]] += dpTen[str(j)]
                dpTen[s[i]] += 1
            return dp
                # print(i, dp[i])

        dp = getDp(s)
        # print(dp[n-1])
        bs = ''
        for i in range(n-1,-1,-1):
            bs += s[i]
        dpBack = getDp(bs)
        # print(dp, dpBack)
        res = 0
        for i in range(2,n-2+1):
            for j in range(10):
                for k in range(10):
                    res += dp[i-1][str(j) + str(k)] * dpBack[n-1-i-1][str(j) + str(k) ]
                    res = res%MOD
                    # print(i, j, k, res)
        return res
    

s = "103301"
s = "000000"
s = "0000000"
sol = Solution()
print(sol.countPalindromes(s))
