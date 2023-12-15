
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
    # 贪心
    def maximumEvenSplit2(self, finalSum: int) -> List[int]:    
        ans = []
        if finalSum%2 == 1:
            return ans
        curr = 2
        while finalSum > 0:
            ans.append(curr)
            finalSum -= curr
            curr += 2
        if finalSum < 0:
            ans[-1] += finalSum
        if len(ans) >= 2 and ans[-1] <= ans[-2]:
            ans[-2] += ans[-1]
            ans.pop()
        return ans
    
    def maximumEvenSplit(self, finalSum: int) -> List[int]:    
        ans = []
        if finalSum%2 == 1:
            return ans
        curr = 2
        while finalSum >= curr:
            ans.append(curr)
            finalSum -= curr
            curr += 2
        ans[-1] += finalSum
        return ans
    
    
finalSum = 28
sol = Solution()
print(sol.maximumEvenSplit2(finalSum))
print(sol.maximumEvenSplit(finalSum))
