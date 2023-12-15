
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
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cache = defaultdict(int)
        ans = 0
        for v in time:
            left = v%60
            ans += cache[(60 - left)%60]
            cache[left] += 1
        return ans
    
time = [30,20,150,100,40]
time = [60,60,60]
sol = Solution()
print(sol.numPairsDivisibleBy60(time))
