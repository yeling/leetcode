
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
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = [] 
        for v in words: 
            temp = v.split(separator)
            for k in temp:
                if len(k) > 0:
                    ans.append(k)

        return ans
    
words = ["one.two.three","four.five","six"]
separator = "."
words = ["$easy$","$problem$"]
separator = "$"
words = ["|||"]
separator = "|"
sol = Solution()
print(sol.splitWordsBySeparator(words, separator))
