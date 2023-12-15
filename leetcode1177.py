
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
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        ans = []
        n = len(s)
        pre = [[0]*26 for _ in range(n + 1)]
        for i in range(n):
            pre[i + 1] = pre[i][:]
            pre[i + 1][ord(s[i]) - 97] += 1

        for l,r,k in queries:
            odd = 0
            for i in range(26):
                if (pre[r + 1][i] - pre[l][i])%2 == 1:
                    odd += 1
            # print(l, r, k, odd)
            ans.append(odd - 1 <= 2*k)
        return ans
    
    
s = "abcda"
queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
sol = Solution()
print(sol.canMakePaliQueries(s, queries))
