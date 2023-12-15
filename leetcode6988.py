
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
    def countPairs2(self, coordinates: List[List[int]], k: int) -> int:  
        n = len(coordinates)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                temp = (coordinates[i][0] ^ coordinates[j][0]) + (coordinates[i][1] ^ coordinates[j][1])
                print(i,j, temp)
                if temp == k:
                    ans += 1 
        return ans
    
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:  
        n = len(coordinates)
        ans = 0
        cache = defaultdict(int)
        # print(c[(5,3)])
        for x,y in coordinates:
            for i in range(k + 1):
                dx = i ^ x
                dy = (k - i) ^ y
                ans += cache[(dx,dy)]
            cache[(x,y)] += 1
        return ans
    
coordinates = [[1,2],[4,2],[1,3],[5,2]]
k = 5
# coordinates = [[1,3],[1,3],[1,3],[1,3],[1,3]]
# k = 0
sol = Solution()
# print(sol.countPairs2(coordinates, k))
print(sol.countPairs(coordinates, k))
