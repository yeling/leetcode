
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
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:  
        if purchaseAmount%10 >= 10 - purchaseAmount%10:
            return 100 - (purchaseAmount//10 + 1)*10
        else:
            return 100 - purchaseAmount//10 * 10
        
    
purchaseAmount = 15
sol = Solution()
print(sol.accountBalanceAfterPurchase(purchaseAmount))
