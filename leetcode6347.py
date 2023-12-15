
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        dst = 'aeiou'
        n = len(words)
        pre = [0] * (n + 1)
        for i,v in enumerate(words):
            fit = 0
            if v[0] in dst and v[-1] in dst:
                fit = 1
            pre[i + 1] = pre[i] + fit
        ans = []
        for l,r in queries:
            ans.append(pre[r+1] - pre[l]);

        return ans
    
words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]
words = ["a","e","i"]
queries = [[0,2],[0,1],[2,2]]
sol = Solution()
print(sol.vowelStrings(words, queries))
