
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
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        n = len(words)
        for i in range(n):
            ln = len(words[i])
            for j in range(i + 1, n):
                if len(words[i]) <= len(words[j]):
                    
                    if words[i] == words[j][0:ln] and words[i] == words[j][-ln:]:
                        ans += 1

        return ans
    
words = ["a","aba","ababa","aa"]
words = ["pa","papa","ma","mama"]
sol = Solution()
print(sol.countPrefixSuffixPairs(words))
