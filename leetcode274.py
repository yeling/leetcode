
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
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans = 0
        for i,v in enumerate(citations):
            if v >= i + 1:
                ans = i + 1
                continue
            else:
                break

        return ans
    
citations = [3,0,6,1,5]
citations = [1,3,1]
sol = Solution()
print(sol.hIndex(citations))
