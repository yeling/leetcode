
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
    def smallestString(self, s: str) -> str:    
        ans = []
        r = -1
        for i, v in enumerate(s):
            if v > 'a':
                ans.append(chr(ord(v) - 1))
                r = i
            elif v == 'a' and r != -1:
                ans += list(s[i:])
                break
            else:
                ans.append(v)
        if s[-1] == 'a' and r == -1:
            ans[-1] = 'z'
        return ''.join(ans)
    
s = "cbabc"
# s = "acbbc"
# s = "leetcode"
s = "a"
# s = "ba"
sol = Solution()
print(sol.smallestString(s))
