
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
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:    
        vis = [[False] * n for _ in range(n)]
        dp = [[] for _ in range(n)]
        def isVis(a, b):
            if len(a) != len(b):
                return False
            diff = 0
            for x,y in zip(a,b):
                if x != y:
                    diff += 1
                    if diff > 1:
                        return False
            return True
        ans = []
        for i in range(n):
            temp = []
            for j in range(0, i):
                if isVis(words[i], words[j]) and groups[i] != groups[j]:
                    if len(dp[j]) > len(temp):
                        temp = dp[j][:]
            temp.append(i)
            dp[i] = temp
            if len(temp) > len(ans):
                ans = temp[:]
            # print(dp)
        ret = []
        for v in ans:
            ret.append(words[v])

        return ret
    
n = 3
words = ["bab","dab","cab"]
groups = [1,2,2]
n = 4
words = ["a","b","c","d"]
groups = [1,2,3,4]

n = 4
words = ["ac","caa","cda","ba"]
groups = [3,1,2,3]

sol = Solution()
print(sol.getWordsInLongestSubsequence(n, words, groups))
