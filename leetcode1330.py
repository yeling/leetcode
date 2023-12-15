
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
    def maxValueAfterReverse2(self, nums: List[int]) -> int:   
        n = len(nums)
        base = 0
        for i in range(1,n):
            base += abs(nums[i] - nums[i-1])
        ans = 0
        for i in range(n):
            for j in range(n):
                if j + 1 < n:
                    if i == 0:
                        ans = max(ans, abs(nums[j+1] - nums[i]) - abs(nums[j + 1] - nums[j]))
                    else:
                        ans = max(ans, abs(nums[j] - nums[i-1]) + abs(nums[j+1] - nums[i]) - abs(nums[i] - nums[i-1]) - abs(nums[j + 1] - nums[j]))
                else:
                    ans = max(ans, abs(nums[j] - nums[i-1]) - abs(nums[i] - nums[i-1]))

        return base + ans
    
    # 25 / 27 
    def maxValueAfterReverse(self, nums: List[int]) -> int:   
        n = len(nums)
        base = 0
        mi = []
        ma = []
        for i in range(1,n):
            base += abs(nums[i] - nums[i-1])
            mi.append(min(nums[i], nums[i-1]))
            ma.append(max(nums[i], nums[i-1]))
        diff = max(0, 2 * (max(mi) - min(ma)))
        #考虑头尾
        for i in range(1,n):
            diff = max(diff, abs(nums[i] - nums[0]) - abs(nums[i] - nums[i-1]))
            diff = max(diff, abs(nums[i-1] - nums[-1]) - abs(nums[i] - nums[i-1]))
        return base + diff
    

nums = [2,3,1,5,4]
nums = [2,3,3,8,4]
nums = [2,5,1,3,4]
sol = Solution()
print(sol.maxValueAfterReverse2(nums))
print(sol.maxValueAfterReverse(nums))
