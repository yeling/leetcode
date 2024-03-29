
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
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    # 578 / 717 个通过测试用例
    # 642 / 717 个通过测试用例
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        ans = 0
        big = []
        small = []
        for v in nums:
            if v ^ k >= v:
                big.append(((v ^ k) - v, v))
            else:
                small.append(((v ^ k) - v, v ))
        # print(big, small)
        if len(big)%2 == 0 or len(small) == 0:
            if len(big)%2 == 0:
                for a,b in big:
                    ans += a + b
            elif len(big)%2 == 1:
                big.sort()
                for i in range(1,len(big)):
                    ans += big[i][0] + big[i][1]
                ans += big[0][1]

            for a,b in small:
                ans += b
        else:
            big.sort()
            small.sort()
            # print(big, small)
            for i in range(1,len(big)):
                ans += big[i][0] + big[i][1]

            if big[0][0]  + small[-1][0]  > 0:
                ans += big[0][0] + big[0][1]
                ans += small[-1][0] + small[-1][1]
                for i in range(len(small) - 2, -1, -1):
                    ans += small[i][1]
            else:
                ans += big[0][1]
                for a,b in small:
                    ans += b
        return ans
    
nums = [1,2,1]
k = 3
edges = [[0,1],[0,2]]
nums = [2,3]
k = 7
edges = [[0,1]]
nums = [7,7,7,7,7,7]
k = 3
edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]

nums = [24,78,1,97,44]
k = 6
edges = [[0,2],[1,2],[4,2],[3,4]]

nums = [49,67,81,34,32]
k = 6
edges = [[1,0],[4,0],[4,2],[3,4]]
#283

sol = Solution()
print(sol.maximumValueSum(nums, k, edges))

