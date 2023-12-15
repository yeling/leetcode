
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

def quickPowMode(a, n, p):
        ans = 1
        while n > 0:
            if n & 1 == 1:
                ans = ans * a % p
            a = a * a % p
            n = n >> 1
        return ans % p

class Solution:
    #1.快速幂
    #2.排序之后双指针
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0 
        right = n - 1
        res = 0
        while left <= right:
            # print(left ,right)
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res += quickPowMode(2, right - left, MOD)
                left += 1

        return res%MOD
    
    def numSubseq2(self, nums: List[int], target: int) -> int:
        #预处理2的幂MOD P 的结果
        cache = [0] * (10 ** 5)
        cache[0] = 1
        for i in range(1, 10 ** 5):
            cache[i] = 2 * cache[i-1]%MOD

        nums.sort()
        n = len(nums)
        left = 0 
        right = n - 1
        res = 0
        while left <= right:
            # print(left ,right)
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res += cache[right - left]
                left += 1

        return res%MOD
    
nums = [2,3,3,4,6,7]
target = 12
nums = [3,5,6,7]
target = 9
sol = Solution()
print(sol.numSubseq2(nums, target))
