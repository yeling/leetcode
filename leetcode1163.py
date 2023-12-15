
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
    # 9 / 33 MLE
    def lastSubstring2(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                stack.append(s[i:j])
        stack.sort()
        # print(stack)
        return stack[-1]
    #11 / 33 TLE
    def lastSubstring3(self, s: str) -> str:
        ans = ''
        n = len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                if ans < s[i:j]:
                    ans = s[i:j]
                elif len(ans) <= j - i:
                    break
                # print(ans, s[i:j])
        # print(stack)
        return ans
    # BFS 按照长度递增
    # 25 / 33
    def lastSubstring4(self, s: str) -> str:
        #BFS （pos, len)
        stack = []
        for i in range(len(s)):
            stack.append((s[i:i+1],i))
        depth = 1
        while len(stack) > 1:
            # print(stack)
            stack.sort()
            last = stack[-1]
            next = []
            i = len(stack) - 1
            depth += 1
            while i >= 0 and stack[i][0] == last[0]:
                next.append((s[stack[i][1]:stack[i][1] + depth],stack[i][1]))
                i -= 1
            stack = next
            
        ans = ''
        if len(stack) == 1:
            ans = s[stack[0][1]:]

        return ans
    #最大字符开始的子串比较，最大的一定到最后了
    def lastSubstring(self, s: str) -> str:
        ans = ''
        c = max(s)
        n = len(s)
        # print(c)
        for i in range(n-1,-1,-1):
            if s[i] == c and ans < s[i:]:
                ans = s[i:]
                # print(ans, s[i:j])
        # print(stack)
        return ans
    
s = "leetcode"
s = "abab"
s = "cacacb"
sol = Solution()
print(sol.lastSubstring2(s))
print(sol.lastSubstring(s))
