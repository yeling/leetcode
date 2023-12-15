
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
    def removeAlmostEqualCharacters(self, word: str) -> int: 
        n = len(word)
        i = 1
        ans = 0
        while i < n:
            if abs(ord(word[i]) - ord(word[i - 1])) <= 1:
                ans += 1
                i += 2
            else:
                i += 1

        return ans
    
word = "aaaaa"
word = "abddez"
word = "zyxyxyz"
sol = Solution()
print(sol.removeAlmostEqualCharacters(word))
