
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
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        r = 0
        ans = 0
        while l < n and r < n:
            if s[l] == '0':
                r = l
                while r < n and s[r] == '0':
                    r += 1
                zero = r - l
                l = r
                while r < n and s[r] == '1':
                    r += 1
                one = r - l
                ans = max(ans, min(one, zero) * 2)
                l = r
            else:
                l += 1
                
        return ans
    
s = "1100000111"
sol = Solution()
print(sol.findTheLongestBalancedSubstring(s))
