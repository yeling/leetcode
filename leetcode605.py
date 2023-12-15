
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
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    # 116 / 127 
    # AC 分类讨论
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans = 0
        cnt = len(flowerbed)
        for i in range(0, cnt):
            if flowerbed[i] == 0 and (i == cnt - 1 or  flowerbed[i + 1] == 0) and (i == 0 or flowerbed[i - 1] == 0):
                flowerbed[i] = 1
                ans += 1

        # print(flowerbed)
            
        return ans >= n
    
flowerbed = [0,0,0,1,0,0,1]
n = 1
flowerbed = [1,0,0,0,1,0,0]
n = 2
sol = Solution()
print(sol.canPlaceFlowers(flowerbed, n))
