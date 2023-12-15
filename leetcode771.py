
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
    def numJewelsInStones(self, jewels: str, stones: str) -> int:  
        ans = 0
        cache = set([v for v in jewels])
        for v in stones:
            if v in cache:
                ans += 1

        return ans
    
jewels = "aA"
stones = "aAAbbbb"
sol = Solution()
print(sol.numJewelsInStones(jewels, stones))
