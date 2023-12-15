
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    # 38 / 77 个通过测试用例
    def isItPossible(self, word1: str, word2: str) -> bool:
        s1 = defaultdict(int)
        s2 = defaultdict(int)
        lower = string.ascii_lowercase
        for v in word1:
            s1[v] += 1
        for v in word2:
            s2[v] += 1
        for i in lower:
            for j in lower:
            	if i in s1 and j in s2:
                    s1[i] -= 1
                    s2[i] += 1
                    s1[j] += 1
                    s2[j] -= 1
                    if s1[i] == 0:
                        del s1[i]
                    if s2[j] == 0:
                        del s2[j]	
                    if len(s1) == len(s2):
                        return True
                    s1[i] += 1
                    s2[i] -= 1
                    s1[j] -= 1
                    s2[j] += 1  
                    if s2[i] == 0:
                        del s2[i]
                    if s1[j] == 0:
                        del s1[j]	          
        return False
        
word1 = "abcc"
word2 = "aab"
# word1 = "abcde"
# word2 = "fghij"
word1 = "ac"
word2 = "b"
sol = Solution()
print(sol.isItPossible(word1, word2))
