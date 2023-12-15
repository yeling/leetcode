
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
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        curr = set()
        all = set()
        for v in arr:
            next = set()
            for k in curr:
                next.add(k | v)
                all.add(k | v)
            next.add(v)
            all.add(v)
            curr = next
        
        return len(all)
    
arr = [1,1,2]
arr = [1,2,4]
sol = Solution()
print(sol.subarrayBitwiseORs(arr))
