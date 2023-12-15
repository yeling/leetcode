
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
    # 68 / 114 个通过测试用例
    def beautifulSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        preCnt = [[0]*20 for _ in range(n + 1)]
        cache = defaultdict(int)
        cache[tuple(preCnt[0])] = 1
        ans = 0
        # print(cache)
        for i,v in enumerate(nums):
            temp = bin(v)[2:]
            for j in range(len(preCnt[i])):
                preCnt[i+1][j] = preCnt[i][j]
            for j in range(len(temp)):
                if temp[-1-j] == '1':
                    preCnt[i+1][j] += 1
                    preCnt[i+1][j] %= 2
            
            ans += cache[tuple(preCnt[i+1])]
            cache[tuple(preCnt[i+1])] += 1
        # print(cache)
        return ans
    
nums = [4,3,1,2,4]
nums = [474,203,603,190,897,875,761,653,769,773,574,275,164,609,648,234,748,439,606,961,746,890,942,838,402,654,21,704,415,903,764,904,573,213,470,450,773,40,364,702,894,326,878]
# nums = [1,10,4]
# nums = [4,3,1,2,3,4,6,8,1,2,3,4]
# nums = [0,0]
sol = Solution()
print(sol.beautifulSubarrays(nums))
