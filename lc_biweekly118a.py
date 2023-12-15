
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
    def findWordsContaining(self, words: List[str], x: str) -> List[int]: 
        ans = []
        for i,v in enumerate(words):
            if x in v:
                ans.append(i)

        return ans
    
words = ["leet","code"]
x = "e"
sol = Solution()
print(sol.findWordsContaining(words, x))
