
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
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int: 
        happiness.sort(reverse=True)
        ans = 0
        for i in range(k):
            ans += max(0, happiness[i] - i)


        return ans
    
happiness = [1,2,3]
k = 2
happiness = [1,1,1,1]
k = 2
happiness = [2,3,4,5]
k = 1
sol = Solution()
print(sol.maximumHappinessSum(happiness, k))
