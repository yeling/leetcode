
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

def quickpower_mod(a, n, mod):
    ans = 1
    while(n != 0):
        if(n & 1):
            ans = (ans * a) % mod
        a = a * a % mod
        n >>= 1
    return ans % mod


class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int: 
        cnt = defaultdict(int)
        sub = 0
        for v in nums:
            cnt[v] += 1
        cache = set()
        curr = defaultdict(int)
        for i,v in enumerate(nums):
            cache.add(v)
            curr[v] += 1
            if curr[v] == cnt[v]:
                cache.remove(v)
            if len(cache) == 0:
                sub += 1
            # print(i,v, sub, curr)

        return quickpower_mod(2,sub - 1,MOD)
    
nums = [1,2,3,4]
# nums = [1,1,1,1]
# nums = [1,2,1,3]
sol = Solution()
print(sol.numberOfGoodPartitions(nums))
