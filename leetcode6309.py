
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

def getAllfactor(k):
    fac = set()
    i = 2
    y = k
    while i <= y:
        # print(i,y)
        if y % i == 0:
            fac.add(i)
            y = y // i
            i = 2
        elif i > sqrt(y):
            fac.add(y)
            break
        else:
            i += 1
    return fac

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * n
        pos = defaultdict(int)

        for i in range(n-1, -1, -1):
            temp = getAllfactor(nums[i])
            # print(temp)
            pre[i] = i
            for tv in temp:
                if tv not in pos:
                    pos[tv] = i
                else:
                    pre[i] = max(pre[i],pos[tv])
        # print(pre)
        r = 0
        for l in range(n):
            r = max(r,pre[l])
            # print(r)
            if l == r and r != n - 1:
                return r
            elif r == n - 1 and l < n - 1:
                return -1
        return -1

nums = [4,7,8,15,3,5]
nums = [4,7,15,8,3,5]
nums = [4,2,8]
# nums = [4,7,15]
sol = Solution()
print(sol.findValidSplit(nums))
