
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
    def findPeaks(self, mountain: List[int]) -> List[int]: 
        ans = []
        n = len(mountain)
        for i in range(1, n -1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                ans.append(i)   
        return ans
    
mountain = [1,4,3,8,5]
sol = Solution()
print(sol.findPeaks(mountain))
