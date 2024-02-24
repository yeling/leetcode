
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
    def lastNonEmptyString(self, s: str) -> str:  
        pos = [[] for _ in range(26)]
        for i,v in enumerate(s):
            pos[ord(v) - ord('a')].append(i)  
        ma = max([len(v) for v in pos])
        ans = []
        for i,v in enumerate(pos):
            if len(v) == ma:
                ans.append((v[-1],chr(i+97)))
        ans.sort()
        ret = ''
        for v in ans:
            ret += v[1]

        # print(ma, ans)
        return ret
    
s = "aabcbbca"
s = "abcdaa"
sol = Solution()
print(sol.lastNonEmptyString(s))
