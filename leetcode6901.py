
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

    def distanceTraveled2(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank > 0:
            ans += 10 * mainTank
            if additionalTank >= mainTank//5:
                additionalTank -= mainTank//5
                mainTank = mainTank//5
            else:
                mainTank = 0

        return ans
    
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank > 0:
            if mainTank >= 5:
                ans += 50
                mainTank -= 5
                if additionalTank > 0:
                    additionalTank -= 1
                    mainTank += 1
            else:
                ans += mainTank*10
                mainTank = 0
        return ans
    
    
    
mainTank = 5
additionalTank = 10
# mainTank = 9
# additionalTank = 2
sol = Solution()
print(sol.distanceTraveled(mainTank, additionalTank))
