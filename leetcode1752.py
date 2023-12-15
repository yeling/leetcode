
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


MOD = 10 ** 9 + 7

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1 or n == 2:
            return True
        count = 0
        for i in range(n):
            if nums[i - 1] > nums[i]:
                count += 1
            if count > 1:
                break
        if count <= 1:
            return True
        else:
            return False
        

sol = Solution()
print()
