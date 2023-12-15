# 939. 最小面积矩形
# auther yeling
from typing import List
from bisect import *
from collections import *

MOD = 10 ** 9 + 7

class Solution:
    #p1, p2 判断p3,p4是否存在
    def minAreaRect2(self, points: List[List[int]]) -> int:
        res = float("inf")
        n = len(points)
        cache = set([str(v[0])+"#"+str(v[1]) for v in points])
        for i in range(n):
            for j in range(i + 1, n):
                if points[i][0] != points[j][0] and points[i][1] != points[j][1] \
                    and str(points[i][0]) + "#" + str(points[j][1]) in cache \
                    and str(points[j][0]) + "#" + str(points[i][1]) in cache :
                    res = min(res, abs(points[i][0] - points[j][0]) * abs(points[i][1] - points[j][1]))         
        if res == float("inf"):
            res = 0
        return res
    def minAreaRect(self, points: List[List[int]]) -> int:
        res = float("inf")
        n = len(points)
        cache = set(map(tuple, points))
        for i in range(n):
            for j in range(i + 1, n):
                if points[i][0] != points[j][0] and points[i][1] != points[j][1] \
                    and (points[i][0],points[j][1]) in cache \
                    and (points[j][0],points[i][1]) in cache :
                    res = min(res, abs(points[i][0] - points[j][0]) * abs(points[i][1] - points[j][1]))         
        if res == float("inf"):
            res = 0
        return res

points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
sol = Solution()
print(sol.minAreaRect(points))
