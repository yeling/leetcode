
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
        # 0,1
        dp = [[] for _ in range(2)]
        for i in range(n):
            next = [[] for _ in range(2)]
            if groups[i] == 0:
                next[0] = dp[1][:]
                next[0].append(i)
                next[1] = dp[1][:]
            elif groups[i] == 1:
                next[1] = dp[0][:]
                next[1].append(i)
                next[0] = dp[0][:]
            dp = next
            # print(dp)
        ans = dp[0]
        if len(dp[1]) > len(dp[0]):
            ans = dp[1]
        ret = []
        for v in ans:
            ret.append(words[v]) 

        return ret
    
n = 3
words = ["e","a","b"]
groups = [0,0,1]
n = 4
words = ["a","b","c","d"]
groups = [1,0,1,1]
sol = Solution()
print(sol.getWordsInLongestSubsequence(n, words, groups))
