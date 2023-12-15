
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        nums = defaultdict(int)
        for v in banned:
            nums[v] = 1
        left = []
        for i in range(1,n+1):
            if nums[i] == 0:
                left.append(i)
        left.sort()
        ss = 0
        
        for i,v in enumerate(left):
            ss += v
            if ss > maxSum:
                return i
        return len(left)
    
banned = [11]
n = 7
maxSum = 50

banned = [1,6,5]
n = 5
maxSum = 6

# banned = [1,2,3,4,5,6,7]
# n = 8
# maxSum = 1

sol = Solution()
print(sol.maxCount(banned, n, maxSum))
