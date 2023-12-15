
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
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:  
        ans = 0
        for v in left:
            ans = max(v, ans)
        for v in right:
            ans = max(n - v, ans)  
        return ans
    
n = 4
left = [4,3]
right = [0,1]

n = 7 
left = []
right = [0,1,2,3,4,5,6,7]
sol = Solution()
print(sol.getLastMoment(n, left, right))
