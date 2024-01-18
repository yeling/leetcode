
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
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def maximumLength(self, s: str) -> int:
        #[][]
        cache = defaultdict(defaultdict)
        n = len(s)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                if j - i + 1 not in cache[s[i]]:
                    cache[s[j]][j - i + 1] = 0
                cache[s[j]][j - i + 1] += 1
                j += 1
            i = j

        # print(cache) 
        ans = -1
        for k in cache:
            ks = list(cache[k].keys())
            ks.sort(reverse=True)
            curr = 0
            for kv in ks:
                curr += cache[k][kv]
                if curr >= 3:
                    ans = max(ans, kv)  
                    break 
        return ans
    
s = "aaaa"
s = "abcdef"
s = "abcaba"
sol = Solution()
print(sol.maximumLength(s))
