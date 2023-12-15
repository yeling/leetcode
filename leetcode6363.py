
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
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cache = defaultdict(int)
        ans = []
        for v in nums:
            cache[v] += 1
        c = 0
        while c  < len(nums):
            temp = []
            for k in list(cache.keys()):
                temp.append(k)
                cache[k] -= 1
                c += 1
                if cache[k] == 0:
                    del cache[k]
            ans.append(temp)
        return ans
    
nums = [1,3,4,1,2,3,1]
nums = [1,2,3,4]
sol = Solution()
print(sol.findMatrix(nums))
