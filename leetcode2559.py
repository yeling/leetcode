
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
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        yuan = set(['a','e','i','o','u'])
        n = len(words)
        pre = [0]*(n+1)
        for i in range(n):
            if words[i][0] in yuan and words[i][-1] in yuan:
                pre[i + 1] = pre[i] + 1
            else:
                pre[i + 1] = pre[i]
        ans = [0] * len(queries)
        for i in range(len(queries)):
            l,r = queries[i]
            ans[i] = pre[r+1] - pre[l]
        return ans
    
words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]
words = ["a","e","i"]
queries = [[0,2],[0,1],[2,2]]
sol = Solution()
print(sol.vowelStrings(words, queries))
