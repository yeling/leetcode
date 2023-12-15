
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
    def minimumSeconds(self, nums: List[int]) -> int:
        cache = defaultdict(list)
        n = len(nums)
        for i,v in enumerate(nums):
            cache[v].append(i)
        print(cache)    
        ans = INF
        for k in cache:
            cnt = len(cache[k])
            temp = 0
            if cnt == 1:
                temp = n - 1
            for i in range(1,cnt):
                temp = max(temp, cache[k][i] - cache[k][i - 1] - 1)
                if i == cnt - 1:
                    temp = max(temp, n + cache[k][0] - cache[k][i] - 1)
            # print(temp)
            ans = min(ans, temp)
        
        return (ans + 1)//2
    
nums = [1,2,1,2]
nums = [2,1,3,3,2]
# nums = [5,5,5,5]
sol = Solution()
print(sol.minimumSeconds(nums))
