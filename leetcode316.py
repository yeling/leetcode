
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    # 166 / 290 
    # 201 / 290 
    # 277 / 290
    # 275 / 290
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = [0] * 26
        for v in s:
            cnt[ord(v) - 97] += 1
        stack = []
        for v in s:
            if v not in stack:
                while len(stack) > 0 and v < stack[-1] and cnt[ord(stack[-1]) - 97] > 0:
                    stack.pop()
                stack.append(v)
            cnt[ord(v) - 97] -= 1 
            print(stack)

        return ''.join(stack)
    
s = "cbacdcbc"
s = "cdadabcc"
s = "bbcaac"
s = "bddbccd"
sol = Solution()
print(sol.removeDuplicateLetters(s))
