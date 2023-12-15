
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
    def squareIsWhite(self, coordinates: str) -> bool:
        x = int(coordinates[1])
        y = ord(coordinates[0]) - 97
        # print(x,y)
        if (x % 2 + y % 2)%2 == 1:
            return False
        else:
            return True
    
coordinates = "e4"
sol = Solution()
print(sol.squareIsWhite(coordinates))
