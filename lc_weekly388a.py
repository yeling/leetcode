
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
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:  
        s = sum(apple)
        capacity.sort(reverse=True)
        for i,v in enumerate(capacity):
            s -= v
            if s <= 0:
                return i + 1  
        return
    
apple = [1,3,2]
capacity = [4,3,1,5,2]
apple = [5,5,5]
capacity = [2,4,2,7]
sol = Solution()
print(sol.minimumBoxes(apple, capacity))
