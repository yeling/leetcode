
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def equalFrequency(self, word: str) -> bool:
        n = len(word)
        for i in range(n):
            cache = defaultdict(int)
            for j in range(n):
                if i != j:
                    cache[word[j]] += 1
            
            allSet = set([cache[k] for k in cache])
            if len(allSet) == 1:
                return True
        
        return False
    
word = "cccddd"
sol = Solution()
print(sol.equalFrequency(word))
