
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
    def incremovableSubarrayCount2(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                left = nums[0:i] + nums[j:n]
                flag = True
                for k in range(1,len(left)):
                    if left[k] > left[k - 1]:
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    ans += 1
                    print(left)    
        return ans
    
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        l = 0
        r = n-1
        for i in range(1,n):
            if nums[i] > nums[i - 1]:
                l = i
                continue
            else:
                break
        for i in range(n -1, 0, -1):
            if nums[i] > nums[i - 1]:
                r = i - 1
                continue
            else:
                break
        # print(l,r)
        if l >= r:
            ans = n * (n + 1)//2
        else:
            ans = 0




               
        return ans
    
nums = [1,2,3,4]
nums = [6,5,7,8]
nums = [3,4,6,5,7,8]
sol = Solution()
print(sol.incremovableSubarrayCount2(nums))

print(sol.incremovableSubarrayCount(nums))
