
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
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        ans = 0
        for i in range(len(processorTime)):
            ans = max(ans , processorTime[i] + tasks[i * 4])
        return ans
    
processorTime = [8,10]
tasks = [2,2,3,1,8,7,4,5]
processorTime = [10,20]
tasks = [2,3,1,2,5,8,4,3]
sol = Solution()
print(sol.minProcessingTime(processorTime, tasks))
