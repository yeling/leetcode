
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
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i]%2 != 0:
                continue
            
            for j in range(i,n):
                flag = True
                for k in range(i,j+1):
                    if k != j and nums[k]%2 == nums[k+1]%2:
                        flag = False
                        break
                    if nums[k] > threshold:
                        flag = False
                        break
                if flag:
                    ans = max(ans, j - i + 1)
        return ans




        return
    
nums = [3,2,5,4]
threshold = 5
nums = [1,2]
threshold = 2
nums = [2,3,4,5]
threshold = 4
sol = Solution()
print(sol.longestAlternatingSubarray(nums, threshold))
