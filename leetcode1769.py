
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


MOD = 10 ** 9 + 7

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = []
        for i in range(n):
            temp = 0
            for j,v  in enumerate(boxes):
                if v == '1':
                    temp += abs(j-i)
            res.append(temp)
        return res

boxes = "001011"
sol = Solution()
print(sol.minOperations(boxes))
