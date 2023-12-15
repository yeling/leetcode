
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
    def sortVowels(self, s: str) -> str:    
        cache = set(['a','e','i','o','u','A','E','I','O','U'])
        yuan = []
        for i,v in enumerate(s):
            if v in cache:
                yuan.append(v)
        l = 0
        ans = []
        yuan.sort() 
        # print(yuan)
        for i,v in enumerate(s):
            if v in cache:
                ans.append(yuan[l])
                l += 1
            else:
                ans.append(v)

        
        return ''.join(ans)
    
s = "lEetcOde"
# s = "lYmpH"
sol = Solution()
print(sol.sortVowels(s))
