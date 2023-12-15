
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
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for v in operations:
            if v == "X++" or v == "++X":
                 ans += 1    
            elif v == "--X" or v == "X--":
                ans -= 1
        return ans
    

operations = ["X++","++X","--X","X--"]
sol = Solution()
print(sol.finalValueAfterOperations(operations))
