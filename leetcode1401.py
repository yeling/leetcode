
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

# 1401. 圆和矩形是否有重叠
# 将圆移动到(0,0),判断四条直线是否在圆内
# 找到矩形中离圆心最近的点
MOD = 10 ** 9 + 7


class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x1 -= xCenter
        y1 -= yCenter
        x2 -= xCenter
        y2 -= yCenter
        x = 0
        y = 0
        #x轴上方，或者下方，y值取最接近轴的
        #如果y1 y2穿过轴了取0，默认值
        if y1 > 0 or y2 < 0:
            y = min(abs(y1), abs(y2))
        
        #如果x1 x2穿过轴了取0，默认值
        #y轴左边，或者右边，y值取最接近轴的
        if x1 > 0 or x2 < 0:
            x = min(abs(x1), abs(x2))

        if y * y + x * x <= radius * radius:
            return True
        return False


radius = 1
x_center = 0
y_center = 0
x1 = -1
y1 = 0
x2 = 0
y2 = 1
sol = Solution()
print(sol.checkOverlap(radius, x_center, y_center, x1, y1, x2, y2))
