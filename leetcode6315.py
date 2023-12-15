
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
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        alpha = ['a','e','i','o','u']
        cnt = 0
        for i in range(left, right+1):
            if words[i][0] in alpha and  words[i][-1] in alpha:
               cnt += 1  
        return cnt
    

words = ["hey","aeo","mu","ooo","artro"]
left = 1
right = 4
sol = Solution()
print(sol.vowelStrings(words, left, right))
