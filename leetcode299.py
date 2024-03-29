
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
    def getHint(self, secret: str, guess: str) -> str:
        scache = [0] * 10
        gcache = [0] * 10
        n = len(secret)
        a = 0
        
        for i in range(n):
            if secret[i] == guess[i]:
                a += 1
            else:
                scache[int(secret[i])] += 1
                gcache[int(guess[i])] += 1
        b = 0
        for i in range(10):
            b += min(scache[i], gcache[i])
            
        return str(a) + "A" + str(b) + "B"
    
secret = "1807"
guess = "7810"
sol = Solution()
print(sol.getHint(secret, guess))
