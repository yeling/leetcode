
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
    def minimumString(self, a: str, b: str, c: str) -> str:
        dst = []
        ans = ''
        if a in b or a in c:
            if b in c:
                return c
            elif c in b:
                return b
            dst = [b, c]
        elif b in a or b in c:
            if a in c:
                return c
            elif c in a:
                return a
            dst = [a, c]
        elif c in a or c in b:
            if a in b:
                return b
            elif b in a:
                return a
            dst = [a, b]
        else:
            dst = [a, b, c]
        cache = []
        for arr in permutations(range(len(dst))):
            temp = [dst[v] for v in arr]
            # print(temp)
            curr = temp[0]
            for i in range(1, len(temp)):
                pos = 0
                for j in range(len(curr) - len(temp[i]), len(curr)):
                    if curr[j:] == temp[i][0:len(curr)-j]:
                        pos = len(curr)-j
                        break
                curr += temp[i][pos:]
            # print(curr)
            cache.append([len(curr), ''.join(curr)])
        cache.sort()
        # print(cache)

        return cache[0][1]
        
        
    
a = "abc"
b = "bca"
c = "aaa"
# a = "ab"
# b = "ba"
# c = "aba"
a = "a"
b = "baa"
c = "aaa"

sol = Solution()
print(sol.minimumString(a,b,c))
