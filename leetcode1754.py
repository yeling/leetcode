
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
    def largestMerge(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        n = len(word1)
        m = len(word2)
        ans = ''
        while i < n or j < m:
            # print(i,j, ans)
            if i < n and j < m:
                if word1[i:] <= word2[j:]:
                    ans += word2[j]
                    j += 1
                else:
                    ans += word1[i]
                    i += 1
            elif i < n:
                ans += word1[i]
                i += 1
            elif j < m:
                ans += word2[j]
                j += 1
        return ans
    
word1 = "cabaa"
word2 = "bcaaa"
word1 = "abcabc"
word2 = "abdcaba"
sol = Solution()
print(sol.largestMerge(word1, word2))
