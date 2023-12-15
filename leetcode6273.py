
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
    def captureForts2(self, forts: List[int]) -> int:
        n = len(forts)
        pre = [0]*n
        for i,v in enumerate(forts):
            if i > 0:
                pre[i] = pre[i - 1]
            if v == 0:
                pre[i] += 1
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (forts[i] == 1 and forts[j] == -1) \
                    or forts[i] == -1 and forts[j] == 1 \
                    and pre[j] - pre[i] == j - i - 1:
                        ans = max(ans, j - i - 1)

        return ans
    
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        pre = [0]*n
        for i,v in enumerate(forts):
            if i > 0:
                pre[i] = pre[i - 1]
            if v == 0:
                pre[i] += 1
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (forts[i] == 1 and forts[j] == -1 \
                    or forts[i] == -1 and forts[j] == 1) \
                    and pre[j] - pre[i] == j - i - 1:
                        ans = max(ans, j - i - 1)

        return ans
    
forts = [1,0,0,-1,0,0,0,0,1]
forts = [1,0,0,-1,0,0,-1,0,0,1]
sol = Solution()
print(sol.captureForts(forts))
