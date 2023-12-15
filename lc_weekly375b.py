
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

def quickpower_mod(a, n, mod):
    ans = 1
    while(n != 0):
        if(n & 1):
            ans = (ans * a) % mod
        a = a * a % mod
        n >>= 1
    return ans % mod

class Solution:
    def getGoodIndices2(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i,(a,b,c,m) in enumerate(variables):
            if pow(pow(a,b)%10,c)%m == target:
                ans.append(i)
        return ans
    
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i,(a,b,c,m) in enumerate(variables):
            if quickpower_mod(quickpower_mod(a,b,10),c,m) == target:
                ans.append(i)
        return ans
    
variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]]
target = 2
# variables = [[39,3,1000,1000]]
# target = 17
sol = Solution()
print(sol.getGoodIndices(variables, target))
