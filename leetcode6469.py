
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
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        cache = set(nums)
        for f,t in zip(moveFrom, moveTo):
            cache.remove(f)
            cache.add(t)
        ans = list(cache)
        ans.sort()
        return ans
    
nums = [1,6,7,8]
moveFrom = [1,7,2]
moveTo = [2,9,5]

nums = [1,1,3,3]
moveFrom = [1,3]
moveTo = [2,2]
sol = Solution()
print(sol.relocateMarbles(nums, moveFrom, moveTo))
