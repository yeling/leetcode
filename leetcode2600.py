
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
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        if k <= numOnes:
            ans = k
        elif k <= numOnes + numZeros:
            ans = numOnes
        else:
            ans = numOnes - (k - numOnes - numZeros )
        
        return ans
    
numOnes = 3
numZeros = 2
numNegOnes = 1
k = 6
sol = Solution()
print(sol.kItemsWithMaximumSum(numOnes, numZeros, numNegOnes,k))
