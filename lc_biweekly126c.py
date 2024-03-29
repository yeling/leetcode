
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
    # 148 / 548 个通过测试用例
    def minimizeStringValue(self, s: str) -> str: 
        cache = [0] * 26
        ans = ""
        for v in s:
            if v == '?':
                cache.sort()
                ans += chr(ord('a') + cache[0][1])
                cache[0][0] += 1
            else:
                
                ans += v
                   
        return ans
    
# s = "????a??aa?b?"
s = "abcdefghijklmnopqrstuvwxy??"
# abcdefghijklmnopqrstuvwxyza
# "abcdefghijklmnopqrstuvwxyaz"
sol = Solution()
print(sol.minimizeStringValue(s))
