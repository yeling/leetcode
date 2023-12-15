
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
    # 6384 / 7414 个通过测试用例
    # AC
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [[0] * 4 for _ in range(n + 1)]
        for i in range(n):
            pre[i + 1] = pre[i][:]
            pre[i + 1][nums[i]] += 1
        pre.append(pre[-1])
        # print(pre)
        ans = INF
        for i in range(n+1):
            for j in range(i,n+1):
                temp = pre[i][2] + pre[i][3]
                if i != j:
                    temp += pre[j + 1][1] - pre[i][1] + pre[j + 1][3] - pre[i][3]
                temp += pre[n][2] - pre[j + 1][2] + pre[n][1] - pre[j + 1][1]
                ans = min(ans, temp)
                # print(i, j, temp, ans)
       
        return ans
    
    
nums = [1,3,2,1,3,3]
nums = [2,1,3,2,1]
nums = [2,2,2,2,3,3]
nums = [3]
sol = Solution()
print(sol.minimumOperations(nums))
