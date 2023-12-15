
# auther yeling
from typing import List
from bisect import *

MOD = 10 ** 9 + 7

class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        n = len(nums)
        cache = list()
        temp = 1
        for i in range(n):
            cache.append(temp)
            temp = (2 * temp) % MOD
        # print(cache)

        nums.sort(reverse=True)
        # print(nums)
        sum = 0
        for i, v in enumerate(nums):
            sum = (sum + (cache[n-1-i]*v) % MOD) % MOD
            sum = (sum + MOD - (cache[i]*v) % MOD) % MOD
        return sum


nums = [2, 1, 3]
nums = [2]
sol = Solution()


print(sol.sumSubseqWidths(nums))
