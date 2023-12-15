
# auther yeling
from typing import List
import math

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : x[1], reverse=True)
        count = 0
        index = 0
        all = 0
        while count < truckSize and index < len(boxTypes):
            count += boxTypes[index][0]
            if count <= truckSize :
                all += boxTypes[index][0] * boxTypes[index][1]
            else :
                all += (truckSize - (count - boxTypes[index][0])) * boxTypes[index][1]
            index += 1
        return all

sol = Solution()


boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
print(sol.maximumUnits(boxTypes, truckSize))
