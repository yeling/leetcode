
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

class Solution:
    def greatestLetter(self, s: str) -> str:
        n = len(s)
        cache = defaultdict(int)
        ans = None
        for i in range(n):
            temp = ord(s[i])
            #a-z
            if temp >= 97 and temp <= 122:
                if cache[temp - 32] != 0 and (ans == None or chr(temp - 32) > ans):
                    ans = chr(temp - 32)
            elif temp >= 65 and temp <= 90:
                if cache[temp + 32] != 0 and (ans == None or chr(temp) > ans):
                    ans = chr(temp)
            cache[temp] = 1
        if ans == None:
            ans = ''
        return ans
    
s = "arRAzFif"
sol = Solution()
print(sol.greatestLetter(s))
