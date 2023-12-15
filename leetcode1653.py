
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
    # 153 / 157
    def minimumDeletions(self, s: str) -> int:
        all = s.count('a')
        n = len(s)
        ans = all
        left = all
        for i,v in enumerate(s):
            if v == 'a':
                left -= 1
            ans = min(ans, left + i + 1 - (all - left))
            
        return ans
    
s = "aababbab"
s = 'bb'
sol = Solution()
print(sol.minimumDeletions(s))
