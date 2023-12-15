
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
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:    
        ans = 0
        n = len(maxHeights)
        for i,v in enumerate(maxHeights):
            curr = v
            height = [0] * n
            height[i] = v
            for j in range(i - 1,-1,-1):
                height[j] = min(height[j + 1], maxHeights[j])
                curr += height[j]
            for j in range(i + 1, n):
                height[j] = min(height[j - 1], maxHeights[j])
                curr += height[j]
            ans = max(ans, curr)
            # print(i,v, height)

        return ans
    
maxHeights = [6,5,3,9,2,7]
maxHeights = [5,3,4,1,1]
maxHeights = [3,2,5,5,2,3]
sol = Solution()
print(sol.maximumSumOfHeights(maxHeights))
