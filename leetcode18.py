
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
from heapq import *
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    #TLE
    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:   
        cache = defaultdict(list)
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j + 1, n):
                    cache[nums[i] + nums[j] + nums[k]].append((i,j,k))
        ans = set()
        # print(cache)
        for i in range(n):
            for a,b,c in cache[target - nums[i]]:
                if i != a and i != b and i != c:
                    temp = [nums[a],nums[b],nums[c],nums[i]]
                    temp.sort()
                    ans.add(tuple(temp))

        return [list(v) for v in ans]
    
    #AC 4s
    def fourSum3(self, nums: List[int], target: int) -> List[List[int]]:   
        cache = defaultdict(list)
        vcache = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j + 1, n):
                    vk = (nums[i], nums[j], nums[k])
                    if vk not in vcache:
                        cache[nums[i] + nums[j] + nums[k]].append((i,j,k))
                        vcache.add(vk)
        ans = set()
        print(cache)
        for i in range(n):
            for a,b,c in cache[target - nums[i]]:
                if i != a and i != b and i != c:
                    temp = [nums[a],nums[b],nums[c],nums[i]]
                    temp.sort()
                    ans.add(tuple(temp))

        return [list(v) for v in ans]
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:   
        cache = defaultdict(list)
        vcache = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                vk = (nums[i], nums[j])
                if vk not in vcache:
                    cache[nums[i] + nums[j]].append((i,j))
                    vcache.add(vk)
        ans = set()
        # print(cache)
        for i in range(n):
            for j in range(i+1, n):
                for a,b in cache[target - nums[i] - nums[j]]:
                    if i != a and i != b and j != a and j != b:
                        temp = [nums[a],nums[b],nums[i],nums[j]]
                        temp.sort()
                        ans.add(tuple(temp))

        return [list(v) for v in ans]
    
    
    
nums = [1,0,-1,0,-2,2]
target = 0

# nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
# target = 8

sol = Solution()
print(sol.fourSum(nums, target))
