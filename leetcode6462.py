
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
    def minimizedStringLength(self, s: str) -> int:
        cache = set()
        for v in s:
            cache.add(v)    
        return len(cache)
    

sol = Solution()
print()
