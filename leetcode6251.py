
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


MOD = 10 ** 9 + 7

class Solution:
    def countPalindromes2(self, s: str) -> int:
        def isHui(s):
            left , right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        allHui = []
        # for i in range(10000,99999):
        #     if isHui(str(i)):
        #         allHui.append(str(i))
        # print(allHui)
        allHui.append('10301')
        ton = [0] * 10
        for v in s:
            ton[int(v)] += 1
        print(ton)
        res = 0
        for v in allHui:
            temp = 1
            for j in range(3):
                temp *= ton[int(j)]
            res = (res + temp)%MOD
        
        return res%MOD

    def countPalindromes(self, s: str) -> int:
        n = len(s)
        dp = [[0] * 100 for _ in range(n)]
        temp = [0] * 10
        for i,v in enumerate(s):
            v = int(v)
            if i == 0:
                temp[v] += 1
            else:
                if i == 3:
                    print(i)
                for j in range(100):
                    dp[i][j] = dp[i - 1][j]
                for j in range(100):
                    dp[i][(j//10) * 10 + v] += dp[i-1][j]
                    dp[i][(j%10) * 10 + v] += dp[i-1][j]
                if i == 1:
                    for j in range(10):
                        dp[i][j*10 + v] += temp[j]               
                # for j in range(100, 110):
                #     dp[i][(j - 100) * 10 + v] += dp[i][j]
                temp[v] += 1
                print(i, dp[i])
        res = 0
        # print(dp)
        for i in range(2, n):
            for j in range(100):
                temp = dp[i - 1][j] * (dp[n-1][(j%10) * 10 + j//10] - dp[i][(j%10) * 10 + j//10])
                # print(i, j, temp)
                res += temp
        return res

s = "103301"
sol = Solution()
print(sol.countPalindromes(s))
