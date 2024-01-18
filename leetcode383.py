
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
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cache = [0] * 26
        for v in magazine:
            cache[ord(v) - ord('a')] += 1
        for v in ransomNote:
            cache[ord(v) - ord('a')] -= 1
            if cache[ord(v) - ord('a')] < 0:
                return False
        return True
    
ransomNote = "aa"
magazine = "aab"
sol = Solution()
print(sol.canConstruct(ransomNote, magazine))
