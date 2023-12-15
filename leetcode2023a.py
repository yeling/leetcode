
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
    def supplyWagon(self, supplies: List[int]) -> List[int]:
        
        n = len(supplies)
        dst = n - n//2
        i = 0
        for i in range(dst):
            temp = supplies[0] + supplies[1]
            pos = 0
            for j in range(1,len(supplies) - 1):
                if temp > supplies[j] + supplies[j + 1]:
                    pos = j
                    temp = supplies[j] + supplies[j + 1]
            if pos == 0:
                supplies = [temp] + supplies[2:]
            else:
                supplies = supplies[0:pos] + [temp] + supplies[pos + 2:]
            # print(supplies)

        return supplies
    
# supplies = [7,3,6,1,8]
# supplies = [1,3,1,5]
supplies = [6,2,2,6,9,8,5,7]
sol = Solution()
print(sol.supplyWagon(supplies))
