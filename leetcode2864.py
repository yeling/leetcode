
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
    def maximumOddBinaryNumber(self, s: str) -> str: 
        n = len(s)
        ans = ""
        one = s.count("1")
        if one == 1:
            ans = "0" * (n - 1) + "1"
        else:
            ans = "1" * (one - 1) + "0" * (n - one) + "1"

        return ans
    
s = "001"
sol = Solution()
print(Solution.maximumOddBinaryNumber(s,s))
# print(sol.maximumOddBinaryNumber(s))
