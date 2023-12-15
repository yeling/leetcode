
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
    #暴力计算所有排列
    def numPermsDISequence2(self, s: str) -> int:
        n = len(s)
        ans = 0
        for seq in permutations(range(n+1)):
            find = True
            for i,v in enumerate(s):
                if v == "D" and seq[i] < seq[i+1]:
                    continue
                elif v == "I" and seq[i] > seq[i+1]:
                    continue
                else:
                    find = False
                    break
            if find:
                ans += 1
        return ans
    
    def numPermsDISequence(self, S: str) -> int:
        MOD = 10**9 + 7
        N = len(S)
        @lru_cache(None)
        def dp(i, j):
            # How many ways to place P_i with relative rank j?
            if i == 0:
                return 1
            elif S[i-1] == 'D':
                return sum(dp(i-1, k) for k in range(j, i)) % MOD
            else:
                return sum(dp(i-1, k) for k in range(j)) % MOD

        return sum(dp(N, j) for j in range(N+1)) % MOD

s = "DIDIDDDI"
sol = Solution()
print(sol.numPermsDISequence2(s))
print(sol.numPermsDISequence(s))
