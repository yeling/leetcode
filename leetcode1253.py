
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

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []
        n = len(colsum)
        ans = [[0]*n for _ in range(2)]
        #先处理2
        for i,v in  enumerate(colsum):
            if v == 2:
                if upper > 0 and lower > 0:
                    ans[0][i] = 1
                    ans[1][i] = 1
                    upper -= 1
                    lower -= 1
                else:
                    return []
        #再处理1
        for i,v in  enumerate(colsum):
            if v == 1:
                if upper > 0:
                    upper -= 1
                    ans[0][i] = 1
                elif lower > 0:
                    lower -= 1
                    ans[1][i] = 1
                else:
                    return []
            # print(upper, lower, ans)
        return ans
    
upper = 2
lower = 1
colsum = [1,1,1]

upper = 5
lower = 5
colsum = [2,1,2,0,1,0,1,2,0,1]

sol = Solution()
print(sol.reconstructMatrix(upper, lower, colsum))
