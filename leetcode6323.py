
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
    # 1522 / 3802
    # 3688 / 3802
    # 3782 / 3802
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children
        if money // 7 >= children:
            if money % 7 == 0 and money // 7 == children: 
                return children
            else:
                return children - 1
        elif money % 7 == 3 and money//7 > 0:
            if money//7 == children - 1:
                return children - 2
            else:
                return money//7
        else:
            return money//7

        
    
# money = 20
# children = 3

# money = 5
# children = 2

money = 23
children = 2

sol = Solution()
print(sol.distMoney(money, children))
