
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
    def countSubstrings(self, s: str, t: str) -> int:
        cache = defaultdict(int)
        for i in range(len(s)):
            for j in range(i, len(s)):
                print(s[i:j+1])
                cache[s[i:j+1]] += 1
        
        print(cache)
        return
    
s = "aba"
t = "baba"
sol = Solution()
print(sol.countSubstrings(s, t))
