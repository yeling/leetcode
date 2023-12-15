
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

    
class Solution:
    def largestValsFromLabels2(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        cache = defaultdict(list)
        n = len(values)
        for i in range(n):
            cache[labels[i]].append(values[i])
        # print(cache)
        # (-maxNumber, labels)
        stack = PriorityQueue()
        for v in cache:
            cache[v].sort(reverse=True)
            # cache[v].sort(reverse=True)
            stack.put((-cache[v][0], v))
        # print(cache)
        cnt = 0
        ans = 0
        check = defaultdict(int)
        while cnt < numWanted and stack.empty() == False:
            curr = stack.get()
            if check[curr[1]] < useLimit:
                check[curr[1]] += 1
                ans += -curr[0]
                cache[curr[1]] = cache[curr[1]][1:]
                if len(cache[curr[1]]) > 0 and check[curr[1]] < useLimit:
                    stack.put((-cache[curr[1]][0],curr[1]))
                # print(curr, check[curr[1]])
                cnt += 1
        return ans
    
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        cache = list()
        n = len(values)
        for i in range(n):
            cache.append((values[i], labels[i]))
            
        cache.sort(reverse=True)
        # print(cache)
        check = [0] * (2*10000 + 1)
        i = 0
        cnt = 0
        ans = 0
        while cnt < numWanted and i < len(cache):
            curr = cache[i]
            if check[curr[1]] < useLimit:
                check[curr[1]] += 1
                ans += curr[0]
                # print(curr, check[curr[1]])
                cnt += 1
            i += 1
        return ans
    
values = [5,4,3,2,1]
labels = [1,3,3,3,2]
numWanted = 3
useLimit = 2

# values = [2,6,1,2,6]
# labels = [2,2,2,1,1]
# numWanted = 1
# useLimit = 1
sol = Solution()
print(sol.largestValsFromLabels(values, labels, numWanted, useLimit))
