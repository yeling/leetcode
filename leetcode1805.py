
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        allNum = []
        word = list(word)
        n = len(word)
        for i in range(n):
            if word[i] >= 'a' and word[i] <= 'z':
                word[i] = ' '
        next = ''
        for v in word:
            next += v
        # print(next.split(' '))
        allNum = set()
        for v in next.split(' '):
            if v.isdigit():
                allNum.add(int(v))
        return len(allNum)

    
    
word = "a0123b012c34d8ef34"
sol = Solution()
print(sol.numDifferentIntegers(word))
