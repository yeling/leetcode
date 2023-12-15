
# auther yeling
from typing import List
from bisect import *
from collections import *

MOD = 10 ** 9 + 7

class Solution:
    #n ^ 2 暴力
    # 43 / 46 
    def numSubarrayBoundedMax2(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)
        sum = 0
        ma = 0
        for i in range(0,n):
            ma = nums[i]
            for j in range(i,n):
                ma = max(ma, nums[j])
                if ma >= left and ma <= right:
                    sum += 1
                elif ma > right:
                    break
        return sum
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)
        sum = 0
        lower = 0 #记录上一个大于right的位置
        upper = -1
        for r in range(0,n):
            #枚举右端点
            if nums[r] >= left and nums[r] <= right:
                upper = r
            if nums[r] > right:
                lower = r + 1
            sum += max(0, upper - lower + 1)
            
        return sum

nums = [2,1,4,3]
left = 2
right = 3
nums = [2,9,2,5,6]
left = 2
right = 8
sol = Solution()
print(sol.numSubarrayBoundedMax2(nums, left, right))
print(sol.numSubarrayBoundedMax(nums, left, right))
