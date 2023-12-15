
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
    
    
    def longestSemiRepetitiveSubstring(self, s: str) -> int: 
        def check(s):
            cnt = 0
            for i in range(1,len(s)):
                if s[i] == s[i-1]:
                    cnt += 1
                if cnt == 2:
                    return i
            return len(s) 
        ans = 0
        n = len(s)
        for i in range(n):
            for j in range(i,n):
                cnt = check(s[i:j+1])
                # print(cnt, s[i:j+1])
                ans = max(ans, cnt)
        return ans
    
    


    
s = "52236443"
# s = "5494"
# s = "1111111" #2
# s = "0001"    #3
sol = Solution()
print(sol.longestSemiRepetitiveSubstring(s))
