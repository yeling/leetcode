
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
    # 498 / 553 个通过测试用例
    # 515 / 553 个通过测试用例
    def findMaximumLength2(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 1
        pre = nums[0]
        i = 1
        while i < n:
            curr = nums[i]
            while i + 1 < n and curr < pre:
                curr += nums[i + 1]
                i += 1
            i += 1
            if curr >= pre:
                cnt += 1
                pre = curr
            else:
                break
 
        return cnt
    
    def findMaximumLength3(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 1
        pre = nums[0]
        i = 1
        while i < n:
            curr = nums[i]
            if curr < pre: 
                flag = False   
                while i + 1 < n and curr < pre:
                    if i + 1 < n and curr + pre <= nums[i + 1]:
                        curr = curr + pre
                        pre = curr
                        flag = True
                        break
                    else:    
                        curr += nums[i + 1]
                        i += 1
                if curr >= pre and flag == False:
                    cnt += 1
                    pre = curr
            else:
                cnt += 1
                pre = curr
            i += 1
            # print(pre)
            
        return cnt
    
    # 498 / 553 个通过测试用例
    # 515 / 553 个通过测试用例
    # 520 / 553 个通过测试用例
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 1
        pre = nums[0]
        i = 1
        while i < n:
            curr = nums[i]
            if curr < pre: 
                flag = False   
                while i + 1 < n and curr < pre:
                    if curr >= pre and curr <= nums[i + 1]:
                        break
                    else:    
                        curr += nums[i + 1]
                        i += 1
                if curr >= pre and flag == False:
                    cnt += 1
                    pre = curr
            else:
                cnt += 1
                pre = curr
            i += 1
            # print(pre)
            
        return cnt
    
nums = [4,3,2,6]
# nums = [1,2,3,4]
# nums = [5,2,2]
# nums = [272,482,115,925,983]
# nums = [1,5,4,9,10]
nums = [171,282,119,154,952,569,633]
nums = [520,531,573,65,426,501,955]
sol = Solution()
print(sol.findMaximumLength(nums))
