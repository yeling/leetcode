
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
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        # 1774. 最接近目标价格的甜点成本
        #1.每份配料三种选择，0,1,2 一共 3^10
        #2.基料，10种选择，直接暴力可以解决，时间复杂度 O(n * 3^m)
        n = len(baseCosts)
        m = len(toppingCosts)

        sel = [[0,1,2] for _ in range(m)]
        res = float('inf')
        temp = 0
        for b in baseCosts:
            for v in product(*sel):
                temp = b
                for i,kv in enumerate(v):
                    temp += toppingCosts[i] * kv
                # print(b, v, temp)
                if abs(temp - target) < abs(res - target):
                    res = temp
                elif abs(temp - target) == abs(res - target) and temp < res:
                    res = temp
        return res
    
baseCosts = [2,3]
toppingCosts = [4,5,100]
target = 18

# baseCosts = [1,7]
# toppingCosts = [3,4]
# target = 10

sol = Solution()
print(sol.closestCost(baseCosts, toppingCosts, target))
