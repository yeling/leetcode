
# auther yeling
from typing import List
import math

class Solution:
    # TLE 179 / 226 
    def isIdealPermutation2(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 2, n):
                if nums[i] > nums[j]:
                    return False
        return True
    
    # AC
    def isIdealPermutation3(self, nums: List[int]) -> bool:
        #排序，比较位置，排序后位置移动超过1，False
        cache = [(i, nums[i]) for i in range(len(nums))]
        cache.sort(key = lambda x : x[1])
        for i in range(len(cache)):
            if abs(cache[i][0] - i) > 1:
                return False
        # print(cache)
        return True
    
    def isIdealPermutation4(self, nums: List[int]) -> bool:
        #记录 i - 2的最大值，大于当前值 False
        mx = 0
        for i in range(2,len(nums)):
            mx = max(mx, nums[i - 2])
            if mx > nums[i]:
                return False
        # print(cache)
        return True
    
    # AC
    def isIdealPermutation(self, nums: List[int]) -> bool:
        #排序，比较位置，排序后位置移动超过1，False
        #排序之后是0--(n - 1)，顺序为自己的值
        # cache = [(i, nums[i]) for i in range(len(nums))]
        # cache.sort(key = lambda x : x[1])
        for i in range(len(nums)):
            if abs(nums[i] - i) > 1:
                return False
        # print(cache)
        return True

sol = Solution()

nums = [1,0,2]
# nums = [1,2,0]
# nums = [2,0,1]
# nums = [1,0,2,3,1]
print(sol.isIdealPermutation(nums))
