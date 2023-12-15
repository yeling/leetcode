
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
    cache = defaultdict(int)
    def solve( nums):
        key = nums
        if key in cache:
            return cache[key]
        ans = 1
        for v in nums:
            ans *= v
        cache[key] = ans
        return ans
    
    

sol = Solution()
print()
