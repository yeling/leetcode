
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
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if prices[0] + prices[1] > money:
            return money
        else:
            return money - prices[0] - prices[1] 
        return
    
prices = [3,2,3]
money = 3
prices = [1,2,2]
money = 3
sol = Solution()
print(sol.buyChoco(prices, money))
