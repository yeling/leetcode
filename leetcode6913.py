
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
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                a = nums[i]
                b = nums[i + 1]
                if b != a + 1:
                    continue
                flag = True
                for k in range(i, j + 1):
                    if (k - i)%2 == 0 and nums[k] == a:
                        continue
                    elif (k - i)%2 == 1 and nums[k] == b:
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    ans = max(ans, j - i + 1)
        if ans == 0:
            ans = -1
        return ans
    
nums = [2,3,4,3,4]
nums = [4,6]
sol = Solution()
print(sol.alternatingSubarray(nums))
