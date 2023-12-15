
# auther yeling
from typing import List
import math
# 92 / 100 
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        allPoints = [[0] * 110 for _ in range(110)]
        # allPoints = [[0] * 5 for _ in range(5)]
        maxValue = 0
        maxP = [0,0]
        for p in towers :
            for xd in range(-radius, radius + 1):
                for yd in range(-radius, radius + 1):
                    if p[0] + xd >= 0 and p[1] + yd >= 0:
                        curr = [p[0] + xd, p[1] + yd]
                        d = math.sqrt(xd * xd + yd * yd)
                        if d > radius:
                            continue
                        allPoints[curr[0]][curr[1]] += p[2] // (1 + d)
                        if allPoints[curr[0]][curr[1]] > maxValue :
                            maxValue = allPoints[curr[0]][curr[1]]
                            maxP = [curr[0], curr[1]]
                        elif allPoints[curr[0]][curr[1]] == maxValue :
                            if curr[0] < maxP[0] or curr[0] == maxP[0] and curr[1] < maxP[1]:
                                maxP = [curr[0], curr[1]]
            # print(maxValue, maxP)
            # print(allPoints)
        return maxP

sol = Solution()

# towers = [[1,2,5],[2,1,7],[3,1,9]] 
# radius = 2
towers = [[23,11,21]]
radius = 9

towers = [[0,1,2],[2,1,2],[1,0,2],[1,2,2]]
radius = 1

print(sol.bestCoordinate(towers,radius))
