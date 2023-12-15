
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
    def pickGifts(self, gifts: List[int], k: int) -> int:
        pq = PriorityQueue()
        for v in gifts:
            pq.put(0-v)
        for _ in range(k):
            top = 0 - pq.get()
            pq.put(-int(sqrt(top)))
        
        ans = 0
       
        while pq.empty() == False:
            top = 0 - pq.get()
            ans += top
        return ans
    
gifts = [25,64,9,4,100]
k = 4
sol = Solution()
print(sol.pickGifts(gifts,k))
