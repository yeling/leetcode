
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string



INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

LOWERS = string.ascii_lowercase

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        n = len(queries)
        ans = [False] * n

        for i,v in enumerate(queries):
            j = 0
            k = 0
            while j < len(v) and k <= len(pattern):
                if k < len(pattern) and v[j] == pattern[k]:
                    j += 1
                    k += 1
                elif v[j] in ascii_lowercase:
                    j += 1
                    continue
                else:
                    break
            ans[i] = j == len(v) and k == len(pattern)

        return ans
    

queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FB"

queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FoBaC"
sol = Solution()
print(sol.camelMatch(queries, pattern))
