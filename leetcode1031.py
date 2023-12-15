
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        dp1 = [[0]*n for _ in range(n)]
        dp2 = [[0]*n for _ in range(n)]
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = nums[i] + pre[i]
        start = min(firstLen, secondLen)
        firstl  = 0
        secondr = 0
        firstr = 0
        secondl = 0
        ans = 0
        for i in range(start, n):
            secondr = 0
            firstr = 0

            # [0,i) l
            for j in range(i-1,firstLen-1 - 1, -1):
                firstl = max(firstl, pre[j+1] - pre[j+1-firstLen])
            # [n - 1, i]
            for j in range(n-1,i - 1 + secondLen - 1, -1):
                secondr = max(secondr, pre[j+1] - pre[j+1-secondLen])
            ans = max(ans, firstl + secondr)
            

            for j in range(i-1,secondLen-1-1, -1):
                secondl = max(secondl, pre[j+1] - pre[j+1-secondLen])
            for j in range(n-1,i - 1 + firstLen - 1, -1):
                firstr = max(firstr, pre[j+1] - pre[j+1-firstLen])
            ans = max(ans, secondl + firstr)
            # print(i, ans)
        return ans
    


nums = [0,6,5,2,2,5,1,9,4]
firstLen = 1
secondLen = 2

nums = [3,8,1,3,2,1,8,9,0]
firstLen = 3
secondLen = 2

nums = [1,0,1]
firstLen = 1
secondLen = 1


sol = Solution()
print(sol.maxSumTwoNoOverlap(nums, firstLen, secondLen))
