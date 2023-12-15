
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
    def similarPairs(self, words: List[str]) -> int:
        cache = [set(v) for v in words]
        cache = [list(v) for v in cache]
        for v in cache:
            v.sort()
        # print(cache)
        n = len(cache)
        ans = 0
        for i in range(n):
            for j in range(i + 1,n):
                if cache[i] == cache[j]:
                    ans += 1         
        return ans
    
words = ["aba","aabb","abcd","bac","aabc"]
sol = Solution()
print(sol.similarPairs(words))
