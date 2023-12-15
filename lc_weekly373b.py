
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
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        yuan = set(['a', 'e', 'i', 'o', 'u'])
        pre = [0] * (n + 2)
        for i in range(n):
            if s[i] in yuan:
                pre[i + 1] = pre[i] + 1
            else:
                pre[i + 1] = pre[i]
        ans = 0
        # print(pre)
        pre[n + 1] = pre[n]
        for i in range(n):
            for j in range(i + 1, n + 1):
                x, y = pre[j] - pre[i], j - i - (pre[j] - pre[i])
                # print(i, j, x, y)
                if x == y and (x * y) %k == 0:
                    ans += 1
        return ans
    
s = "baeyh"
k = 2
s = "abba"
k = 1
s = "bcdf"
k = 1
sol = Solution()
print(sol.beautifulSubstrings(s, k))
