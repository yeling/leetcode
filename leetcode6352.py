
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
    # 33 / 1294 个通过测试用例 TLE
    def beautifulSubsets2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(1,1<<n):
            cache = [False] * 2000
            find = True
            for j in range(n):
                if i & (1<<j) != 0:
                    if cache[nums[j] + 1000] == False:
                        cache[nums[j] + 1000 + k] = True
                        cache[nums[j] + 1000 - k] = True
                    else:
                        find = False
                        break
            if find:
                ans += 1
                # print(bin(i))
        return ans
    
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        global ans
        ans = 0
        def dfs(index, path):
            global ans
            if index == n:
                # print(index, path)
                if len(path) > 0:
                    ans += 1
                return 
            #不要
            dfs(index + 1, path)
            #要
            for v in path:
                if v == nums[index] + k or  v == nums[index] - k:
                    return
            next = path[:]
            next.append(nums[index])
            dfs(index + 1, next)
            return 
        dfs(0, [])
        return ans
    
nums = [2,4,6]
k = 2
sol = Solution()
print(sol.beautifulSubsets(nums, k))
