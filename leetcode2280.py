
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


MOD = 10 ** 9 + 7

EPS = 1e-9
def fequal(x, y):
    return abs(x - y) < EPS


class Solution:
    # 73 / 82
    # float有精度损失，改为整数乘法
    def minimumLines2(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort(key=lambda x: x[0])
        res = 0
        k = 0
        print(stockPrices)
        for i in range(1, len(stockPrices)):
            if i == 1:
                dy = stockPrices[i][1] - stockPrices[i-1][1]
                dx = stockPrices[i][0] - stockPrices[i-1][0]
                k = dy / dx
                res = 1
            else:
                dy = stockPrices[i][1] - stockPrices[i-1][1]
                dx = stockPrices[i][0] - stockPrices[i-1][0]
                temp = dy / dx
                if not fequal(temp,k):
                    res += 1
                    k = temp
        return res
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort(key=lambda x: x[0])
        res = 0
        dx = 0
        dy = 0
        print(stockPrices)
        for i in range(1, len(stockPrices)):
            if i == 1:
                dy = stockPrices[i][1] - stockPrices[i-1][1]
                dx = stockPrices[i][0] - stockPrices[i-1][0]
                res = 1
            else:
                dy1 = stockPrices[i][1] - stockPrices[i-1][1]
                dx1 = stockPrices[i][0] - stockPrices[i-1][0]
                if dx * dy1 != dy * dx1:
                    res += 1
                    dx = dx1
                    dy = dy1
        return res
         
    
stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]
stockPrices = [[3,4],[1,2],[7,8],[2,3]]
stockPrices = [[1,1000000000],[1000000000,1000000000],[999999999,1],[2,999999999]]
sol = Solution()

print(sol.minimumLines(stockPrices))
