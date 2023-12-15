
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        cache = defaultdict(int)
        left = 0
        right = 0
        curr = 0
        while right < n:
            curr += cache[nums[right]]
            cache[nums[right]] += 1
            while curr >= k:
                ans += n - 1 - right + 1
                if cache[nums[left]] >= 2:
                    curr -= cache[nums[left]] - 1
                cache[nums[left]] -= 1
                left += 1       
            right += 1
        return ans
    
nums = [3,1,4,3,2,2,4]
k = 2
nums = [1,1,1,1,1]
k = 10
sol = Solution()
print(sol.countGood(nums,k))
