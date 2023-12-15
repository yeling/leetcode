
# auther yeling
from typing import List
from bisect import *
from collections import *

MOD = 10 ** 9 + 7

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j + 1, n):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        res += 1

        return res

nums = [4,4,2,4,3]
nums = [1,1,1,1,1]
nums = [2,1,1]
sol = Solution()
print(sol.unequalTriplets(nums))
