
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
    def maximumLength(self, nums: List[int]) -> int:
        cache = defaultdict(int)
        for v in nums:
            cache[v] += 1
        ans = 1
        ks = list(cache.keys())
        ks.sort()
        flag = defaultdict(bool)
        ans = max(1, cache[1] - (cache[1] + 1)%2)

        for i in range(len(ks)):
            if ks[i] in flag or ks[i] == 1:
                continue
            curr = ks[i]
            cn = 0
            while curr <= ks[-1] and curr in cache:
                cn += 1
                if cache[curr] >= 2:
                    flag[curr] = True
                    curr = curr * curr
                    continue
                else:
                    break
            ans = max(2 * cn - 1, ans)
            # print(ans, i)

        return ans
    
nums = [5,4,1,2,2]
nums = [1,3,2,4]
nums = [1,1]
nums = [1,16,49,16,121]
sol = Solution()
print(sol.maximumLength(nums))
