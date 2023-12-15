
# auther yeling
from typing import List
from bisect import *
from collections import *

MOD = 10 ** 9 + 7

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        cache = defaultdict(int)
        for v in nums:
            cache[v] += 1
        if any(cache[key] > k for key in cache):
            return -1
        

        return

nums = [6,3,8,1,3,1,2,2]
k = 4
nums = [5,3,3,6,3,3]
k = 3
sol = Solution()
print(sol.minimumIncompatibility(nums, k))
