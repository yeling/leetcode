
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
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        global numIndex
        numIndex = defaultdict(int)
        global dp
        global ans
        
        dp = [[] for _ in range(n)]
        for i in range(n):
            numIndex[arr[i]] = i
            for j in range(i + 1,n):
                if arr[j]%arr[i] == 0:
                    dp[j].append(i)
        
        @cache
        def dfs(index):
            # print("dfs", index)
            global dp
            temp = 1
            for v in dp[index]:
                if arr[v] > int(sqrt(arr[index])):
                    break 
                if arr[index]//arr[v] in numIndex:
                    # print("dfs", index)
                    if arr[v] == arr[index]//arr[v]:
                        temp += dfs(v) * dfs(numIndex[arr[index]//arr[v]])
                    else:
                        temp += 2 * dfs(v) * dfs(numIndex[arr[index]//arr[v]])
            return temp%MOD

        ans = 0
        for i in range(n):
            ans += dfs(i)
            ans %= MOD

        return ans
    
arr = [2, 4, 5, 10]
arr = [2, 4]
sol = Solution()
print(sol.numFactoredBinaryTrees(arr))
