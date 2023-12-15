
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
    def isAcronym(self, words: List[str], s: str) -> bool: 
        if len(s) != len(words):
            return False
        for i,v in enumerate(words):
            if s[i] == v[0]:
                continue
            else:
                return False   
        return True
    
words = ["alice","bob","charlie"]
s = "abc"
words = ["an","apple"]
s = "a"
sol = Solution()
print(sol.isAcronym(words,s))
