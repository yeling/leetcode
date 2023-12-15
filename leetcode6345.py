
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
    # 18 / 36 个通过测试用例
    def minCost2(self, basket1: List[int], basket2: List[int]) -> int:
        all = defaultdict(int)
        for v in basket1:
            all[v] += 1
        for v in basket2:
            all[v] += 1
        dst = []
        for k in all:
            if all[k]%2 != 0:
                return -1
            else:
                for i in range(all[k]//2):
                    dst.append(k)
        
        ans = 0
        
        basket1.sort()
        dst.sort()
        print(basket1)
        print(dst)
        for i in range(len(basket1)):
            if basket1[i] != dst[i]:
                ans += min(basket1[i], dst[i])
            
        return ans
    # 33 / 36 个通过测试用例
    def minCost3(self, basket1: List[int], basket2: List[int]) -> int:
        all = defaultdict(int)
        for v in basket1:
            all[v] += 1
        for v in basket2:
            all[v] += 1
        minNum = INF
        for k in all:
            minNum = min(minNum, k)
            if all[k]%2 != 0:
                return -1
            else:
                all[k] //=2
        ans = 0
        dst = basket1
        if minNum in basket2:
            dst = basket2
        for v in dst:
            if all[v] > 0:
                all[v] -= 1
            else:
                if v == minNum:
                    ans += minNum
                else:
                    ans += 2 * minNum
        return ans
    
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        all = defaultdict(int)
        for v in basket1:
            all[v] += 1
        for v in basket2:
            all[v] += 1
        minNum = INF
        for k in all:
            minNum = min(minNum, k)
            if all[k]%2 != 0:
                return -1
            else:
                all[k] //=2
        ans = 0
        need = []
        for v in basket1:
            if all[v] > 0:
                all[v] -= 1
            else:
                need.append(v)
        for v in all:
            if all[v] > 0:
                for i in range(all[v]):
                    need.append(v)
        need.sort()
        for i in range(len(need)//2):
            if need[i] > 2 * minNum:
                ans += 2 * minNum
            else:
                ans += need[i]
        return ans
basket1 = [4,2,2,2]
basket2 = [1,4,1,2]
# basket1 = [2,3,4,1]
# basket2 = [3,2,5,1]
# basket1 = [84,80,43,8,80,88,43,14,100,88]
# basket2 = [32,32,42,68,68,100,42,84,14,8]
# basket1 = [4,4,4,4,3]
basket2 = [5,5,5,5,3]

sol = Solution()
print(sol.minCost(basket1, basket2))
