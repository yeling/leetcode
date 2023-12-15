
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
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:    
        ans = s[:]
        k = len(indices)
        cache = list(zip(indices, sources, targets))
        cache.sort()
        # print(cache)
        for i in range(k-1, -1, -1):
            indice, source, target = cache[i]
            if s[indice:indice + len(source)] == source:
                ans = ans[0:indice] + target + ans[indice+len(source):]
            # print(ans)
        return ans
    
s = "vmokgggqzp"
indexes = [3,5,1]
sources = ["kg","ggq","mo"]
targets = ["s","so","bfr"]
sol = Solution()
print(sol.findReplaceString(s, indexes, sources, targets))
