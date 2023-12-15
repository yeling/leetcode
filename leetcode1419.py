
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
    # 59 / 60 
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        #croak
        ans = 0
        busy = 0
        cache = defaultdict(int)
        for v in croakOfFrogs:
            if v == 'c':
                busy += 1
                ans = max(ans, busy)
                cache[v] += 1
            elif v == 'r':
                if cache['c'] > 0:
                    cache['c'] -= 1
                    cache['r'] += 1
                else:
                    return -1
            elif v == 'o':
                if cache['r'] > 0:
                    cache['r'] -= 1
                    cache['o'] += 1
                else:
                    return -1
            elif v == 'a':
                if cache['o'] > 0:
                    cache['o'] -= 1
                    cache['a'] += 1
                else:
                    return -1
            elif v == 'k':
                if cache['a'] > 0:
                    cache['a'] -= 1
                    cache['k'] += 1
                    busy -= 1
                else:
                    return -1
        if cache['c'] != 0 or cache['r'] != 0 or cache['o'] != 0 or cache['a'] != 0:
            ans = -1
        
        return ans
    
croakOfFrogs = "crcoakroak"
croakOfFrogs = "croakcroak"
# croakOfFrogs = "croakroak"
sol = Solution()
print(sol.minNumberOfFrogs(croakOfFrogs))
