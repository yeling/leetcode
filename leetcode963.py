
# auther yeling
# 963. 最小面积矩形 II
from typing import List
from bisect import *
from collections import *
from math import *
from itertools import *

MOD = 10 ** 9 + 7

class Solution:
    # 103 / 109 
    #以0为顶点的三条线，矩形的三条对边相等
    #面积为三个变成乘起来，除以最长的边
    def minAreaFreeRect2(self, points: List[List[int]]) -> float:
        def dis(a,b):
            dx = abs(a[0] - b[0])
            dy = abs(a[1] - b[1])
            return sqrt(dx * dx + dy * dy)
        n = len(points)
        res = float('inf')
        for a in range(n):
            for b in range(a + 1,n):
                for c in range(b + 1,n):
                    for d in range(c + 1,n):
                        rect = [points[a],points[b],points[c],points[d]]
                        #以0为顶点的三条线，矩形的三条对边相等
                        #面积为三个变成乘起来，除以最长的边
                        x = dis(rect[0], rect[1])
                        y = dis(rect[0], rect[2])
                        z = dis(rect[0], rect[3])
                        if x == dis(rect[2], rect[3]) and y == dis(rect[1], rect[3]) and z == dis(rect[1], rect[2]):
                            s = x * y * z / max(x,y,z)
                            res = min(res, s)
        if res == float(inf):
            res = 0
        return res
    #任意两个点的中心点相同，对角线长相同，可以组成矩形
    #(p+dis, c) key = p + dis 
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        def dis(a,b):
            dx = abs(a[0] - b[0])
            dy = abs(a[1] - b[1])
            return sqrt(dx * dx + dy * dy)
        n = len(points)
        res = float('inf')
        cache = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                a, b = points[i], points[j]
                if a != b:
                    c = [(a[0] + b[0])/2, (a[1] + b[1])/2]
                    d = dis(a,b)
                    # print(c[0])
                    k = str(c[0]) + "#" + str(c[1]) + '#' + str(d)
                    cache[k].append(a)
        # print(cache)
        for k in cache:
            for it in permutations(cache[k], 2):
                d = [float(v) for v in k.split("#")]
                d1 = dis(it[0], it[1])
                p3 = [d[0] + d[0] - it[0][0], d[1] + d[1] - it[0][1]]
                d2 = dis(it[1], p3)
                res = min(res, d1 * d2)
                # print(it)
        if res == float(inf):
            res = 0
        return res

# points = [[1,2],[2,1],[1,0],[0,1]]
points = [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
# points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
sol = Solution()
print(sol.minAreaFreeRect(points))

