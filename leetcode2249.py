
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

# 2249. 统计圆内格点数目
MOD = 10 ** 9 + 7

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        allPoints = set()
        for v in circles:
            start = (v[0] - v[2],v[1] - v[2])
            end = (v[0] + v[2],v[1] + v[2])
            for dst in product(list(range(start[0], end[0] + 1)), list(range(start[1], end[1] + 1))):
                # print(dst)
                dx = dst[0] - v[0]
                dy = dst[1] - v[1]
                if dx * dx + dy * dy <= v[2] * v[2]:
                    allPoints.add(dst)
        return len(allPoints)

circles = [[2,2,1]]
circles = [[2,2,2],[3,4,1]]

sol = Solution()
print(sol.countLatticePoints(circles))
