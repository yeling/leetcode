
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


MOD = 10 ** 9 + 7

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        preN = [0] * (n + 1)
        afterY = [0] * (n + 1)
        for i in range(n):
            if customers[i] == 'N':
                preN[i] = preN[i - 1] + 1
            else:
                preN[i] = preN[i - 1]
        preN[n] = preN[n - 1]
        for i in range(n-1, -1, -1):
            if customers[i] == 'Y':
                if i == n - 1:
                    afterY[i] = 1
                else:
                    afterY[i] = afterY[i+1] + 1
            else:
                if i == n - 1:
                    afterY[i] = 0
                else:
                    afterY[i] = afterY[i+1]

        # print(preN, afterY)
        c = 10 ** 5
        res = -1
        for i in range(n + 1):
            temp = 0
            if i == 0:
                temp = afterY[i]
            else:
                temp = afterY[i] + preN[i - 1]
            if temp < c:
                c = temp
                res = i
            # print(i , temp)

        return res

customers = "YYNY"
# customers = "NNNNN"
# customers = "YYYY"
sol = Solution()
print(sol.bestClosingTime(customers))
