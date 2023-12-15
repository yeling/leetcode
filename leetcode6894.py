
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
    def sumImbalanceNumbers2(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1,n):
                temp = nums[i: j + 1]
                temp.sort()
                # print(temp)
                for k in range(1, len(temp)):
                    if temp[k] - temp[k - 1] > 1:
                        ans += 1

        return ans
    
    # 513 / 1303
    # 698 / 1303 个通过测试用例
    # AC n^2 * log(n) 
    # 这里的插入操作，如果是linkedlist插入很快的
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            cache = [nums[i]]
            temp = 0
            for j in range(i + 1,n):
                pos = bisect(cache, nums[j])
                if pos == len(cache):
                    if nums[j] - cache[-1] > 1:
                        temp += 1
                    cache.append(nums[j])
                elif pos == 0:
                    if cache[0] - nums[j] > 1:
                        temp += 1
                    cache = [nums[j]] + cache
                else:
                    if cache[pos] - cache[pos - 1] > 1:
                        temp -= 1
                    if nums[j] - cache[pos - 1] > 1:
                        temp += 1
                    if cache[pos] - nums[j] > 1:
                        temp += 1
                    cache = cache[0:pos] + [nums[j]] + cache[pos:]
                ans += temp

        return ans
    
# nums = [1,3,3,3,5]
nums = [2,3,1,4,1,4,5]
nums = [1,3,2,2]
sol = Solution()
print(sol.sumImbalanceNumbers2(nums))
print(sol.sumImbalanceNumbers(nums))
