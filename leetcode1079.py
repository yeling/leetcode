
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:    
        arr = [v for v in tiles]
        cache = set()
        for i in range(1,len(arr) + 1):
            for v in permutations(arr,i):
                # print(v)
                cache.add(v)
        return len(cache)
    
tiles = "AAABBC"
sol = Solution()
print(sol.numTilePossibilities(tiles))
