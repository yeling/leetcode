
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
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        pre = [0] * n
        after = [0] * n
        stack = []
        #(value, cnt)
        sum = 0
        for i,v in enumerate(maxHeights):
            cnt = 1
            while len(stack) > 0 and stack[-1][0] >= v:
                cnt += stack[-1][1]
                sum -= stack[-1][0] * stack[-1][1]
                stack.pop()
            sum += v * cnt
            pre[i] = sum
            stack.append((maxHeights[i], cnt))
        
        sum = 0
        stack = []
        maxHeights = maxHeights[::-1]
        for i,v in enumerate(maxHeights):
            cnt = 1
            while len(stack) > 0 and stack[-1][0] >= v:
                cnt += stack[-1][1]
                sum -= stack[-1][0] * stack[-1][1]
                stack.pop()
            sum += v * cnt
            after[i] = sum
            stack.append((maxHeights[i], cnt))
        after = after[::-1]
        maxHeights = maxHeights[::-1]
        # print(pre, after)
        ans = max(pre[i] + after[i] - maxHeights[i] for i in range(n))
        
        return ans
    
maxHeights = [6,5,3,9,2,7]
sol = Solution()
print(sol.maximumSumOfHeights(maxHeights))
