
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
    def circularGameLosers(self, n: int, k: int) -> List[int]:    
        cache = [0]*(n)
        i = 0 
        s = 0
        while True:
            dst = (s + i*k)%n
            cache[dst] += 1
            if cache[dst] == 2:
                break
            s = (s + i*k)%n
            i += 1
            # print(i, s, cache)
        ans = [i+1 for i,v in enumerate(cache) if v == 0]
        return ans
    
n = 4
k = 4
n = 5
k = 2
sol = Solution()
print(sol.circularGameLosers(n,k))
