
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
    # TLE
    def countTriplets2(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                ans += n * n
                continue
            for j in range(n):
                if nums[i] & nums[j] == 0:
                    ans += n
                    continue
                for k in range(n):
                    if nums[i] & nums[j] & nums[k] == 0:
                        ans += 1


        return ans
    
    def countTriplets3(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        cache = defaultdict(int)
        for i in range(n):
            for j in range(n):
                cache[nums[i] & nums[j]] += 1

        for k in cache:
            for v in nums:
                if k & v == 0:
                    ans += cache[k]
                
        return ans
    
    def countTriplets(self, nums: List[int]) -> int:
        cnt = [0] * (1 << 16)
        for x in nums:
            for y in nums:
                cnt[x & y] += 1
        ans = 0
        for m in nums:
            m ^= 0xffff
            s = m
            print('begin' ,m, s)
            while True:  # 枚举 m 的子集（包括空集）
                ans += cnt[s]
                s = (s - 1) & m
                print(s)
                if s == m: break
        return ans

    def countTriplets(self, nums: List[int]) -> int:
        #计算补集的子集，数量累加
        cnt = [0] * (1 << 16)
        for x in nums:
            for y in nums:
                cnt[x & y] += 1
        ans = 0
        for m in nums:
            m ^= 0xffff
            s = m
            # print('begin' ,m, s)
            while s:  # 枚举 m 的子集（包括空集）
                ans += cnt[s]
                s = (s - 1) & m
                # print(s)
            ans += cnt[0]
                
        return ans

nums = [2,1,3]
sol = Solution()
print(sol.countTriplets3(nums))
print(sol.countTriplets(nums))
