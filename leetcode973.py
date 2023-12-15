
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue



MOD = 10 ** 9 + 7

# 973. 最接近原点的 K 个点
class Solution:
    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        all = []
        for v in points:
            dis = v[0] * v[0] + v[1] * v[1]
            all.append((dis,v))
        
        all.sort(key = lambda x : x[0])
        print(all)
        res = []
        for i in range(k):
            res.append(all[i][1])
        return res
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        all = PriorityQueue()
        for v in points:
            dis = v[0] * v[0] + v[1] * v[1]
            all.put((dis,v))
        
        print(all.qsize())
        
        res = []
        for _ in range(k):
            res.append(all.get()[1])
        return res
    
points = [[1,3],[-2,2]]
k = 1

points = [[3,3],[5,-1],[-2,4]]
k = 2

sol = Solution()
print(sol.kClosest(points, k))
