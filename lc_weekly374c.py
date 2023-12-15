
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
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        l = 0 
        r = 0
        n = len(word)
        ans = 0
        mi = word[l]
        ma = word[l]
        while r < n:
                
        return
    
word = "igigee"
k = 2
sol = Solution()
print(sol.countCompleteSubstrings(word, k))
