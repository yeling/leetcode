
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
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        pre = set()
        after = defaultdict(int)
        n = len(nums)
        ans = [0]*n
        for v in nums:
            after[v] += 1
        # print(after)
        # after.remove(nums[0])
        for i in range(n):
            # print(pre, after)
            pre.add(nums[i])
            if nums[i] in after:
                if after[nums[i]] == 1:
                    del after[nums[i]]
                else:
                    after[nums[i]] -= 1
            ans[i] = len(pre) - len(after)
            
        return ans
    
nums = [3,2,3,4,2]
nums = [1,2,3,4,5]
sol = Solution()
print(sol.distinctDifferenceArray(nums))
