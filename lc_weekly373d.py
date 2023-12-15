
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
    def beautifulSubstrings2(self, s: str, k: int) -> int:
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
        
        pre[n + 1] = pre[n]
        cache = []
        for i in range(1, pre[n] + 1):
            if (i * i) % k == 0:
                cache.append(i)
        
        print(pre, cache)
        
        for i in range(n):
            curr = pre[i]
            for v in cache:
                a = bisect_left(pre, curr + v)
                if a == n:
                    break
                b = bisect_left(pre, curr + v + 1)
                if b == n + 1:
                    break
                c = bisect_left(pre, curr + 2 * v)
                if c == n + 1:
                    break
                d = bisect_left(pre, curr + 2 * v + 1)
                if 2 *a > d or 2 * b < c:
                    break
                else:
                    ans += 1
            print(i, ans)
                
            
        return ans
    
s = "baeyh"
k = 2
s = "abba"
k = 1
# s = "bcdf"
# k = 1
sol = Solution()
print(sol.beautifulSubstrings2(s, k))
print(sol.beautifulSubstrings(s, k))
