
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
    def makeSmallestPalindrome(self, s: str) -> str:   
        l = 0
        r = len(s) - 1
        ans = [''] * (len(s))
        while l <= r:
            if s[l] != s[r]:
                temp = min(s[l], s[r])
                ans[l] = ans[r] = temp 
            else:
                ans[l] = ans[r] = s[r]
            l += 1
            r -= 1
        return ''.join(ans)
    
s = "egcfe"
s = "abcd"
s = "seven"
sol = Solution()
print(sol.makeSmallestPalindrome(s))
