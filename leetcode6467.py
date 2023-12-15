
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
    # 1344 / 1421 个通过测试用例
    # 1384 / 1421 个通过测试用例
    # AC
    # 分桶，滑动窗口
    def longestEqualSubarray(self, nums: List[int], k: int) -> int: 
        cache = defaultdict(deque)
        preSum = defaultdict(int)
        ans = 1
        for i,v in enumerate(nums):
            curr = cache[v]
            if len(curr) == 0:
                preSum[v] = 0
                cache[v].append(i)
            else:
                preSum[v] += i - curr[-1] - 1
                cache[v].append(i)
                if preSum[v] > k:
                    while preSum[v] > k and len(cache[v]) > 1:
                        preSum[v] -= cache[v][1] - cache[v][0] - 1
                        cache[v].popleft()
                
                ans = max(ans, len(cache[v]))
                

        return ans
    
nums = [1,3,2,3,1,3]
k = 3
nums = [1,1,2,2,1,1]
k = 2
nums = [1,2,1]
k = 0

sol = Solution()
print(sol.longestEqualSubarray(nums, k))
