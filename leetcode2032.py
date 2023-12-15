
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
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)
        all = set(nums1 + nums2 + nums3)
        ans = []
        for v in all:
            temp = 0
            if v in s1:
                temp += 1
            if v in s2:
                temp += 1
            if v in s3:
                temp += 1
            if temp >= 2:
                ans.append(v)

        # print(all)
        return ans
    
nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3,4]
sol = Solution()
print(sol.twoOutOfThree(nums1, nums2, nums3))
